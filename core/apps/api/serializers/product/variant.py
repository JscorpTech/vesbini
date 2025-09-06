from rest_framework import serializers

from core.apps.api.models import ProductVariantModel
from core.apps.api.serializers.product.color import ListColorSerializer
from core.apps.api.serializers.product.size import ListSizeSerializer


class BaseProductVariantSerializer(serializers.ModelSerializer):
    size = ListSizeSerializer()
    color = ListColorSerializer()

    class Meta:
        model = ProductVariantModel
        fields = [
            "id",
            "color",
            "size",
            "amount",
        ]


class ListProductVariantSerializer(BaseProductVariantSerializer):
    class Meta(BaseProductVariantSerializer.Meta): ...


class MiniProductVariantSerializer(BaseProductVariantSerializer):
    class Meta(BaseProductVariantSerializer.Meta):
        fields = [
            "id",
            "color",
            "size",
        ]


class RetrieveProductVariantSerializer(BaseProductVariantSerializer):
    class Meta(BaseProductVariantSerializer.Meta):
        fields = [
            "id",
            "color",
            "size",
            "amount",
            "quantity",
        ]


class CreateProductVariantSerializer(BaseProductVariantSerializer):
    class Meta(BaseProductVariantSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
