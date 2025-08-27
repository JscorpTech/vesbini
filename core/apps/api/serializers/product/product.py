from rest_framework import serializers

from core.apps.api.models import ProductModel
from core.apps.api.serializers.product.color import ListColorSerializer
from core.apps.api.serializers.product.size import ListSizeSerializer


class BaseProductSerializer(serializers.ModelSerializer):
    colors = ListColorSerializer(many=True)
    sizes = ListColorSerializer(many=True)

    class Meta:
        model = ProductModel
        fields = [
            "id",
            "title",
            "desc",
            "image",
        ]


class ListProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta): ...


class RetrieveProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta):
        fields = [
            "id",
            "title",
            "desc",
            "image",
            "colors",
            "sizes",
        ]


class CreateProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta):
        fields = [
            "id",
        ]
