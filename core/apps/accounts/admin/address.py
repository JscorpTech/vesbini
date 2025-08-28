from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.accounts.models import DistrictModel, RegionModel


@admin.register(RegionModel)
class RegionAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(DistrictModel)
class DistrictAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
