from rest_framework import serializers

from core.apps.accounts.models import RegionModel


class BaseRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionModel
        fields = [
            "id",
            "name",
        ]


class ListRegionSerializer(BaseRegionSerializer):
    class Meta(BaseRegionSerializer.Meta): ...


class RetrieveRegionSerializer(BaseRegionSerializer):
    class Meta(BaseRegionSerializer.Meta): ...


class CreateRegionSerializer(BaseRegionSerializer):
    class Meta(BaseRegionSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
