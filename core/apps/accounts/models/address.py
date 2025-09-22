from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class CountryModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)
    flag = models.ImageField(_("flag"), upload_to="flag/", null=True, blank=False)
    code = models.CharField(_("code"), max_length=10, null=True, blank=False)

    def __str__(self):
        return str(self.name)

    @classmethod
    def _create_fake(cls):
        return cls.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "country"
        verbose_name = _("CountryModel")
        verbose_name_plural = _("CountryModels")


class RegionModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)
    country = models.ForeignKey("CountryModel", on_delete=models.CASCADE, null=True, blank=False)

    def __str__(self):
        return str(self.name)

    @classmethod
    def _create_fake(cls):
        return cls.objects.create(
            name="mock",
            country=CountryModel._create_fake(),
        )

    class Meta:
        db_table = "region"
        verbose_name = _("RegionModel")
        verbose_name_plural = _("RegionModels")
