from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.decorators import display

from core.apps.api.models import RetailShiftModel, StoreModel


@admin.register(StoreModel)
class StoreAdmin(ModelAdmin):
    list_display = ("id", "name", "is_default")

    @display(description="is default", boolean=True)
    def is_default(self, obj):
        return obj.default


@admin.register(RetailShiftModel)
class RetailshiftAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
        "updated_at",
        "created_at",
    )
