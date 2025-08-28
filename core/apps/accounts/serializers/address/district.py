from rest_framework import serializers

from core.apps.accounts.models import DistrictModel


class BaseDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistrictModel
        fields = [
            "id",
            "name",
        ]


class ListDistrictSerializer(BaseDistrictSerializer):
    class Meta(BaseDistrictSerializer.Meta): ...


class RetrieveDistrictSerializer(BaseDistrictSerializer):
    class Meta(BaseDistrictSerializer.Meta): ...


class CreateDistrictSerializer(BaseDistrictSerializer):
    class Meta(BaseDistrictSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
