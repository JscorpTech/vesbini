from rest_framework import serializers

from core.apps.api.models import BasketModel
from core.apps.api.models.product import ColorModel, ProductVariantModel, SizeModel
from core.apps.api.serializers.product.product import MiniProductSerializer
from core.apps.api.serializers.product.variant import MiniProductVariantSerializer


class BaseBasketSerializer(serializers.ModelSerializer):
    product = MiniProductSerializer()
    variant = MiniProductVariantSerializer()
    amount = serializers.SerializerMethodField()

    def get_amount(self, obj) -> int:
        return obj.variant.amount  # type: ignore

    def validate(self, attr):  # type: ignore
        if "color" in attr and "size" not in attr:
            raise serializers.ValidationError({"size": "Size is required"})
        if "size" in attr and "color" not in attr:
            raise serializers.ValidationError({"color": "Color is required"})
        if "color" in attr and "size" in attr:
            variant = ProductVariantModel.objects.filter(
                color=attr.pop("color"), size=attr.pop("size"), product=attr.get("product")
            ).first()
            if variant is None:
                raise serializers.ValidationError({"variant": ["Variant not found"]})
            if variant.quantity <= 0:
                raise serializers.ValidationError({"variant": ["The item is not available in stock."]})
            attr["variant"] = variant
        return attr

    class Meta:
        model = BasketModel
        fields = [
            "id",
            "product",
            "count",
            "amount",
            "variant",
        ]


class ListBasketSerializer(BaseBasketSerializer):
    class Meta(BaseBasketSerializer.Meta): ...


class RetrieveBasketSerializer(BaseBasketSerializer):
    class Meta(BaseBasketSerializer.Meta): ...


class CreateBasketSerializer(BaseBasketSerializer):
    product = None
    color = serializers.PrimaryKeyRelatedField(queryset=ColorModel.objects.all(), required=True, write_only=True)
    size = serializers.PrimaryKeyRelatedField(queryset=SizeModel.objects.all(), required=True, write_only=True)

    def to_representation(self, instance):
        return {"id": instance.id}

    def create(self, validated_data):
        validated_data["user"] = self.context.get("request").user  # type: ignore
        return BasketModel.objects.create(**validated_data)

    class Meta(BaseBasketSerializer.Meta):
        fields = [
            "id",
            "product",
            "count",
            "color",
            "size",
        ]


class UpdateBasketSerializer(BaseBasketSerializer):
    product = None
    color = serializers.PrimaryKeyRelatedField(queryset=ColorModel.objects.all(), write_only=True)
    size = serializers.PrimaryKeyRelatedField(queryset=SizeModel.objects.all(), write_only=True)

    def to_representation(self, instance):
        return {"detail": "updated"}

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    class Meta(BaseBasketSerializer.Meta):
        fields = [
            "id",
            "product",
            "count",
            "color",
            "size",
        ]
