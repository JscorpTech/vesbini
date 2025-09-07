import logging
from itertools import islice

from celery import shared_task

from core.apps.api.models.moysklad import RetailShiftModel
from core.apps.api.models.product import ProductVariantModel
from core.apps.api.services.moysklad import active_retailshift
from core.services.moysklad import MoySklad


def chunked(queryset, n=50):
    it = iter(queryset)
    while True:
        chunk = list(islice(it, n))
        if not chunk:
            break
        yield chunk


@shared_task
def moysklad():
    service = MoySklad()
    products = ProductVariantModel.objects.filter(sku__isnull=False, href__isnull=False).values_list("sku", flat=True)
    for chunk in chunked(products):
        try:
            for code, quantity, href in service.stok(hrefs=chunk):
                ProductVariantModel.objects.filter(sku=code).update(quantity=quantity, href=href)
        except Exception as e:
            logging.error(e)
    products = ProductVariantModel.objects.filter(sku__isnull=False, href__isnull=True).values_list("sku", flat=True)
    for chunk in chunked(products):
        try:
            for code, quantity, href in service.stok(chunk):
                ProductVariantModel.objects.filter(sku=code).update(quantity=quantity, href=href)
        except Exception as e:
            logging.error(e)

    print("updated")


@shared_task
def retailshift():
    service = MoySklad()
    old_retailshift = active_retailshift()
    if old_retailshift is not None:
        service.close_retailshift(old_retailshift.href)
    retailshift = service.create_retailshift()
    RetailShiftModel.objects.create(href=retailshift, is_active=True)
