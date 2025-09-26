from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import PromocodeModel


@receiver(post_save, sender=PromocodeModel)
def PromocodeSignal(sender, instance, created, **kwargs): ...
