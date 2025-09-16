from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class BotUser(AbstractBaseModel):
    LANG = (
        ("uz", "uz"),
        ("ru", "ru"),
        ("en", "en"),
    )
    chat_id = models.CharField(
        verbose_name=_("chat id"),
        max_length=255,
        unique=True,
    )
    is_register = models.BooleanField(_("is register"), default=False)
    phone = models.CharField(_("phone"), max_length=255, null=True, blank=True)
    full_name = models.CharField(_("full name"), max_length=255, null=True, blank=True)
    lang = models.CharField(
        _("lang"),
        max_length=255,
        choices=LANG,
        default="uz",
    )

    def __str__(self) -> str:
        return "%s - %s" % (self.full_name, self.phone)


class Messages(AbstractBaseModel):
    key = models.CharField(_("key"), max_length=255)
    value = models.TextField(_("value"))

    def __str__(self):
        return "%s - %s" % (self.key, self.value)

    class Meta:
        db_table = "messages"
        verbose_name = _("messages")
        verbose_name_plural = _("messages")
