from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import ItemModel, OrderModel


@receiver(post_save, sender=OrderModel)
def OrderSignal(sender, instance, created, **kwargs): ...


@receiver(post_save, sender=ItemModel)
def ItemSignal(sender, instance, created, **kwargs): ...
