from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin

from core.apps.accounts.models import CountryModel, RegionModel


@admin.register(CountryModel)
class CountryAdmin(TabbedTranslationAdmin, ModelAdmin):
    search_fields = ["name"]
    list_display = (
        "id",
        "name",
        "created_at",
    )


@admin.register(RegionModel)
class RegionAdmin(TabbedTranslationAdmin, ModelAdmin):
    search_fields = ["name", "country__name"]
    list_display = (
        "id",
        "name",
        "country__name",
        "created_at",
    )
