from rest_framework import serializers

from core.apps.api.models import PromocodeModel


class BasePromocodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromocodeModel
        fields = [
            "id",
            "name",
        ]


class ListPromocodeSerializer(BasePromocodeSerializer):
    class Meta(BasePromocodeSerializer.Meta): ...


class RetrievePromocodeSerializer(BasePromocodeSerializer):
    class Meta(BasePromocodeSerializer.Meta): ...


class CreatePromocodeSerializer(BasePromocodeSerializer):
    class Meta(BasePromocodeSerializer.Meta):
        fields = [
            "id",
            "name",
        ]


class CheckPromocodeSerializer(BasePromocodeSerializer):
    class Meta(BasePromocodeSerializer.Meta):
        fields = [
            "code",
            "discount",
            "promo_type",
        ]
