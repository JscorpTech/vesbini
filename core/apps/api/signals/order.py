from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import ItemModel, OrderModel
from core.apps.api.services.moysklad import default_store
from core.apps.api.tasks.moysklad import order_moysklad
from core.services.moysklad import MoySklad


@receiver(post_save, sender=OrderModel)
def OrderSignal(sender, instance, created, **kwargs):
    if instance.payment_status and not instance._payment_status and instance.is_delivery:
        order_moysklad.delay(instance)


@receiver(post_save, sender=ItemModel)
def ItemSignal(sender, instance, created, **kwargs): ...
