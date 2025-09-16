from rest_framework import serializers

from core.apps.api.models import NotificationModel


class BaseNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationModel
        fields = ["id", "title", "desc", "image", "created_at", "updated_at"]


class ListNotificationSerializer(BaseNotificationSerializer):
    class Meta(BaseNotificationSerializer.Meta): ...


class RetrieveNotificationSerializer(BaseNotificationSerializer):
    class Meta(BaseNotificationSerializer.Meta): ...


class CreateNotificationSerializer(BaseNotificationSerializer):
    class Meta(BaseNotificationSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
