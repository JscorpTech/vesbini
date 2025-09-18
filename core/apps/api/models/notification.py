from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel

User = get_user_model()


class NotificationModel(AbstractBaseModel):
    title = models.CharField(_("title"), max_length=255)
    desc = models.TextField(_("desc"))
    image = models.ImageField(_("image"), upload_to="notification/", null=True, blank=True)

    def __str__(self):
        return str(self.title)

    @classmethod
    def _create_fake(cls):
        return cls.objects.create(
            title="test",
            desc="test",
        )

    class Meta:
        db_table = "notification"
        verbose_name = _("NotificationModel")
        verbose_name_plural = _("NotificationModels")


class UserNotificationModel(AbstractBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification = models.ForeignKey("NotificationModel", on_delete=models.CASCADE)
    is_read = models.BooleanField(_("is read"), default=False)

    def __str__(self):
        return str(self.notification.title)

    @classmethod
    def _create_fake(cls):
        return cls.objects.create(
            user=User._create_fake(),
            notification=NotificationModel._create_fake(),
        )

    class Meta:
        db_table = "usernotification"
        verbose_name = _("UsernotificationModel")
        verbose_name_plural = _("UsernotificationModels")
