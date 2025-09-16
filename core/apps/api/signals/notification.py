from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import NotificationModel, UserNotificationModel


@receiver(post_save, sender=NotificationModel)
def NotificationSignal(sender, instance, created, **kwargs):
    if created:
        objects = []
        for user in get_user_model().objects.all():
            objects.append(UserNotificationModel(user=user, notification=instance))
        UserNotificationModel.objects.bulk_create(objects)


@receiver(post_save, sender=UserNotificationModel)
def UsernotificationSignal(sender, instance, created, **kwargs): ...
