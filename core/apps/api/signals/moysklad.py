from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import RetailshiftModel, StoreModel


@receiver(post_save, sender=StoreModel)
def StoreSignal(sender, instance, created, **kwargs):
    if instance.default:
        StoreModel.objects.filter(default=True).exclude(pk=instance.pk).update(default=False)


@receiver(post_save, sender=RetailshiftModel)
def RetailshiftSignal(sender, instance, created, **kwargs):
    if instance.is_active:
        RetailshiftModel.objects.filter(is_active=True).exclude(pk=instance.pk).update(is_active=False)
