from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import DeliveryMethodModel


@receiver(post_save, sender=DeliveryMethodModel)
def DeliverymethodSignal(sender, instance, created, **kwargs): ...
