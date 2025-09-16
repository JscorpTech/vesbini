from rest_framework import serializers

from core.apps.api.models import UserNotificationModel
from core.apps.api.serializers.notification.notification import (
    ListNotificationSerializer,
    RetrieveNotificationSerializer,
)


class BaseUsernotificationSerializer(serializers.ModelSerializer):
    notification = ListNotificationSerializer()

    class Meta:
        model = UserNotificationModel
        fields = [
            "id",
            "notification",
            "is_read",
        ]


class ListUsernotificationSerializer(BaseUsernotificationSerializer):
    class Meta(BaseUsernotificationSerializer.Meta): ...


class RetrieveUsernotificationSerializer(BaseUsernotificationSerializer):
    notification = RetrieveNotificationSerializer()

    class Meta(BaseUsernotificationSerializer.Meta): ...


class CreateUsernotificationSerializer(BaseUsernotificationSerializer):
    class Meta(BaseUsernotificationSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
