from rest_framework import serializers

from core.apps.api.models import DeliveryMethodModel


class BaseDeliveryMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryMethodModel
        fields = [
            "id",
            "name",
        ]


class ListDeliveryMethodSerializer(BaseDeliveryMethodSerializer):
    class Meta(BaseDeliveryMethodSerializer.Meta): ...


class RetrieveDeliveryMethodSerializer(BaseDeliveryMethodSerializer):
    class Meta(BaseDeliveryMethodSerializer.Meta): ...


class CreateDeliveryMethodSerializer(BaseDeliveryMethodSerializer):
    class Meta(BaseDeliveryMethodSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
