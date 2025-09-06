from rest_framework import serializers

from core.apps.api.models import ProductImageModel
from core.apps.api.serializers.product.color import ListColorSerializer


class BaseProductImageSerializer(serializers.ModelSerializer):
    color = ListColorSerializer()

    class Meta:
        model = ProductImageModel
        fields = [
            "color",
            "image",
        ]


class ListProductImageSerializer(BaseProductImageSerializer):
    class Meta(BaseProductImageSerializer.Meta): ...


class RetrieveProductImageSerializer(BaseProductImageSerializer):
    class Meta(BaseProductImageSerializer.Meta): ...


class CreateProductImageSerializer(BaseProductImageSerializer):
    class Meta(BaseProductImageSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
