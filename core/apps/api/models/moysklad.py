from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class StoreModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)
    moysklad_id = models.CharField(_("moysklad id"), max_length=255)
    default = models.BooleanField(_("default"), default=False)

    def __str__(self):
        return str(self.name)

    @classmethod
    def _create_fake(cls):
        return cls.objects.create(
            name="mock",
            moysklad_id="12121",
        )

    class Meta:
        db_table = "store"
        verbose_name = _("StoreModel")
        verbose_name_plural = _("StoreModels")


class RetailShiftModel(AbstractBaseModel):
    href = models.CharField(_("mys id"), max_length=255)
    is_active = models.BooleanField(_("is active"), default=False)

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            mys_id="mock",
        )

    class Meta:
        db_table = "retailshift"
        verbose_name = _("RetailshiftModel")
        verbose_name_plural = _("RetailshiftModels")
