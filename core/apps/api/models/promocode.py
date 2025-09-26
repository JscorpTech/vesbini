from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel

from core.apps.api.enums.promocode import PromocodeTypeEnum


class PromocodeModel(AbstractBaseModel):
    code = models.CharField(_("promocode"), max_length=50)
    quantity = models.BigIntegerField(_("quantity"), default=1)
    discount = models.BigIntegerField(_("discount"))
    promo_type = models.CharField(
        _("promocode"), max_length=20, choices=PromocodeTypeEnum.choices, default=PromocodeTypeEnum.FIXED.value
    )

    def __str__(self):
        return str(self.code)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            code="JST",
            quantity=100,
            discount=100,
            promo_type=PromocodeTypeEnum.FIXED.value,
        )

    class Meta:
        db_table = "promocode"
        verbose_name = _("PromocodeModel")
        verbose_name_plural = _("PromocodeModels")
