from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from core.apps.api.models import FeedbackModel
from core.apps.api.models.notification import NotificationModel, UserNotificationModel


@receiver(post_save, sender=FeedbackModel)
def FeedbackSignal(sender, instance, created, **kwargs):
    if not created and instance._answer is None and instance.answer is not None:
        notification = NotificationModel.objects.create(
            title=_("Feedback"),
            desc=instance.answer,
        )
        UserNotificationModel.objects.create(
            user=instance.user,
            notification=notification,
        )
