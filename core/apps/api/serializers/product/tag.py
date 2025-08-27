from rest_framework import serializers

from core.apps.api.models import TagModel


class BaseTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagModel
        fields = [
            "id",
            "name",
        ]


class ListTagSerializer(BaseTagSerializer):
    class Meta(BaseTagSerializer.Meta): ...


class RetrieveTagSerializer(BaseTagSerializer):
    class Meta(BaseTagSerializer.Meta): ...


class CreateTagSerializer(BaseTagSerializer):
    class Meta(BaseTagSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
