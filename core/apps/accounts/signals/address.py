from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.accounts.models import RegionModel, CountryModel


@receiver(post_save, sender=CountryModel)
def RegionSignal(sender, instance, created, **kwargs): ...


@receiver(post_save, sender=RegionModel)
def DistrictSignal(sender, instance, created, **kwargs): ...
