from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.accounts.models import CountryModel, RegionModel


@admin.register(CountryModel)
class CountryAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(RegionModel)
class RegionAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
