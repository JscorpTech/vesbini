from rest_framework import serializers

from core.apps.api.models import ColorModel


class BaseColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorModel
        fields = [
            "id",
            "name",
        ]


class ListColorSerializer(BaseColorSerializer):
    class Meta(BaseColorSerializer.Meta): ...


class RetrieveColorSerializer(BaseColorSerializer):
    class Meta(BaseColorSerializer.Meta): ...


class CreateColorSerializer(BaseColorSerializer):
    class Meta(BaseColorSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
