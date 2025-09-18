import logging
from itertools import islice

from celery import shared_task
from httpx._transports import default

from core.apps.api.models.moysklad import RetailShiftModel, StoreModel
from core.apps.api.models.order import OrderModel
from core.apps.api.models.product import ProductVariantModel
from core.apps.api.services.moysklad import active_retailshift, default_store
from core.services.moysklad import MoySklad


def chunked(queryset, n=50):
    it = iter(queryset)
    while True:
        chunk = list(islice(it, n))
        if not chunk:
            break
        yield chunk


@shared_task
def stores():
    service = MoySklad()
    stores = service.get_stores()
    for store in stores:
        StoreModel.objects.update_or_create(
            href=store.get("href"),
            defaults={
                "name": store.get("name"),
            },
        )
    logging.info("Stores updated")


@shared_task
def moysklad():
    service = MoySklad()
    # products = ProductVariantModel.objects.filter(sku__isnull=False, href__isnull=False).values_list("sku", flat=True)
    # for chunk in chunked(products):
    #     try:
    #         for code, quantity, href in service.stok(hrefs=chunk):
    #             ProductVariantModel.objects.filter(sku=code).update(quantity=quantity, href=href)
    #     except Exception as e:
    #         logging.error(e)
    products = ProductVariantModel.objects.filter(sku__isnull=False).values_list("sku", "is_bundle")
    for chunk in chunked(products):
        try:
            for code, quantity, href in service.stok(chunk[0], kind="bundle" if chunk[1] else "product"):
                ProductVariantModel.objects.filter(sku=code).update(quantity=quantity, href=href)
        except Exception as e:
            logging.error(e)

    print("updated")


@shared_task
def retailshift():
    service = MoySklad()
    old_retailshift = active_retailshift()
    if old_retailshift is not None:
        service.close_retailshift(old_retailshift)
    retailshift = service.create_retailshift()
    RetailShiftModel.objects.create(href=retailshift, is_active=True)


@shared_task(bind=True, max_retries=5)
def order_moysklad(self, order_id):
    try:
        order = OrderModel.objects.get(pk=order_id)
    except OrderModel.DoesNotExist:
        return
    if order.href is not None:
        print("order already created")
        return
    service = MoySklad()
    products = []
    if order.items.count() == 0:
        print("No items in order")
        return self.retry(countdown=300)
    for item in order.items.all():
        products.append(
            {
                "quantity": item.count,
                "price": item.amount * 100,
                "assortment": {
                    "meta": {
                        "href": item.variant.href,
                        "type": "bundle" if item.variant.is_bundle else "product",
                    }
                },
            }
        )
    try:
        order.href = service.create_order(products, default_store())
        order.save()
    except Exception as e:
        print("error", e)
        return self.retry(countdown=300)
