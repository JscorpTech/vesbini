from django.db import models
from rest_framework import serializers

from core.apps.api.models import ProductModel
from core.apps.api.serializers.product.productimage import ListProductImageSerializer
from core.apps.api.serializers.product.variant import RetrieveProductVariantSerializer


class BaseProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        fields = [
            "id",
            "title",
            "desc",
            "image",
        ]


class ListProductSerializer(BaseProductSerializer):
    variants = RetrieveProductVariantSerializer(many=True)
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
            "variants",
        ]


class MiniProductSerializer(BaseProductSerializer):

    def get_amount(self, obj):
        return obj.variants.aggregate(amount__min=models.Min("amount"))["amount__min"]

    class Meta(BaseProductSerializer.Meta):
        fields = [
            "id",
            "title",
            "image",
        ]


class RetrieveProductSerializer(BaseProductSerializer):
    variants = RetrieveProductVariantSerializer(many=True)
    images = ListProductImageSerializer(many=True)

    class Meta(BaseProductSerializer.Meta):
        fields = [
            "id",
            "title",
            "desc",
            "image",
            "variants",
            "images",
        ]


class CreateProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta):
        fields = [
            "id",
        ]
