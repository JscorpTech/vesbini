from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import PromocodeModel


@admin.register(PromocodeModel)
class PromocodeAdmin(ModelAdmin):
    list_display = (
        "id",
        "code",
        "quantity",
        "promo_type",
        "created_at",
        "updated_at",
    )
