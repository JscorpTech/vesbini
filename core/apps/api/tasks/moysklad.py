import logging
from itertools import islice

from celery import shared_task

from core.apps.api.models.product import ProductVariantModel
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
    products = ProductVariantModel.objects.filter(sku__isnull=False).values_list("sku", flat=True)
    for chunk in chunked(products):
        try:
            for code, quantity in service.stok(chunk):
                ProductVariantModel.objects.filter(sku=code).update(quantity=quantity)
        except Exception as e:
            logging.error(e)

    print("updated")
