from django.db import models
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
    amount = serializers.SerializerMethodField()

    def get_amount(self, obj):
        return obj.variants.aggregate(amount__min=models.Min("amount"))["amount__min"]

    class Meta(BaseProductSerializer.Meta):
        fields = [
            "id",
            "title",
            "desc",
            "image",
            "amount",
        ]


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
