from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import FeedbackModel


@admin.register(FeedbackModel)
class FeedbackAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
