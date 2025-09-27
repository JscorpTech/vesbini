from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.payment.models import HistoryModel


@admin.register(HistoryModel)
class HistoryAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
