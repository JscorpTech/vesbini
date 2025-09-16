from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import NotificationModel, UserNotificationModel


@admin.register(NotificationModel)
class NotificationAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(UserNotificationModel)
class UsernotificationAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
