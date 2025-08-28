from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.accounts.models import DistrictModel, RegionModel


@receiver(post_save, sender=RegionModel)
def RegionSignal(sender, instance, created, **kwargs): ...


@receiver(post_save, sender=DistrictModel)
def DistrictSignal(sender, instance, created, **kwargs): ...
