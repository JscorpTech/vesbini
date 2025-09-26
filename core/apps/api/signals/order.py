from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import ItemModel, OrderModel
from core.apps.api.services.order import cancel_order, confirm_order


@receiver(post_save, sender=OrderModel)
def OrderSignal(sender, instance, created, **kwargs):
    if instance.payment_status and not instance._payment_status and instance.is_delivery:
        confirm_order(instance)
    elif not instance.payment_status and instance._payment_status:
        cancel_order(instance)


@receiver(post_save, sender=ItemModel)
def ItemSignal(sender, instance, created, **kwargs): ...
