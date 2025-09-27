from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.payment.models import HistoryModel


@receiver(post_save, sender=HistoryModel)
def HistorySignal(sender, instance, created, **kwargs): ...
