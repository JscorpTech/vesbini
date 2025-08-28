from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class RegionModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(cls):
        return cls.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "region"
        verbose_name = _("RegionModel")
        verbose_name_plural = _("RegionModels")


class DistrictModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)
    region = models.ForeignKey("RegionModel", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(cls):
        return cls.objects.create(
            name="mock",
            region=RegionModel._create_fake(),
        )

    class Meta:
        db_table = "district"
        verbose_name = _("DistrictModel")
        verbose_name_plural = _("DistrictModels")
