from rest_framework import serializers

from core.apps.api.models import ItemModel
from core.apps.api.serializers.product.product import ListProductSerializer
from core.apps.api.serializers.product.variant import ListProductVariantSerializer


class BaseItemSerializer(serializers.ModelSerializer):
    product = ListProductSerializer()
    variant = ListProductVariantSerializer()

    class Meta:
        model = ItemModel
        fields = [
            "id",
            "product",
            "count",
            "variant",
            "amount",
        ]


class ListItemSerializer(BaseItemSerializer):
    class Meta(BaseItemSerializer.Meta): ...


class RetrieveItemSerializer(BaseItemSerializer):
    class Meta(BaseItemSerializer.Meta): ...


class CreateItemSerializer(BaseItemSerializer):
    class Meta(BaseItemSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
