from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin

from core.apps.api.models import DeliveryMethodModel


@admin.register(DeliveryMethodModel)
class DeliverymethodAdmin(TabbedTranslationAdmin, ModelAdmin):
    list_display = ("id", "name", "price", "updated_at", "created_at")
