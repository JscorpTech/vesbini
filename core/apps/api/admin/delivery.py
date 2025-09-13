from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import DeliveryMethodModel


@admin.register(DeliveryMethodModel)
class DeliverymethodAdmin(ModelAdmin):
    list_display = ("id", "name", "updated_at", "created_at")
