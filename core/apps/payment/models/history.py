from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel

User = get_user_model()


class HistoryModel(AbstractBaseModel):
    TYPE = (
        ("income", _("income")),
        ("outcome", _("outcome")),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.BigIntegerField(_("amount"), default=0)
    type = models.CharField(_("type"), max_length=255, default="income", choices=TYPE)
    comment = models.CharField(_("comment"), max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(cls):
        return cls.objects.create(
            user=User._create_fake(),
            amount=100,
            type="income",
            comment="salom",
        )

    class Meta:
        db_table = "history"
        verbose_name = _("HistoryModel")
        verbose_name_plural = _("HistoryModels")
