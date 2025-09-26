from django.db.transaction import atomic
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from core.apps.api.models import OrderModel
from core.apps.api.models.moysklad import StoreModel
from core.apps.api.models.order import ItemModel
from core.apps.api.models.product import BasketModel
from core.apps.api.serializers.order.item import ListItemSerializer
from core.apps.api.services.order import confirm_order
from core.apps.api.tasks.moysklad import order_moysklad


class BaseOrderSerializer(serializers.ModelSerializer):
    items = ListItemSerializer(many=True)

    class Meta:
        model = OrderModel
        fields = [
            "id",
            "items",
            "status",
            "payment_status",
            "amount",
            "delivery_method",
            "address",
            "is_delivery",
        ]


class ListOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta): ...


class RetrieveOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta): ...


class CreateOrderSerializer(BaseOrderSerializer):
    items = serializers.ListField(
        child=serializers.PrimaryKeyRelatedField(queryset=BasketModel.objects.all()), write_only=True
    )

    def validate(self, attrs):
        if attrs.get("is_delivery", False):
            if attrs.get("delivery_method") is None:
                raise serializers.ValidationError({"delivery_method": [_("Delivery method field is required")]})
        return attrs

    def to_representation(self, instance):
        return {"id": instance.id}

    def create(self, validated_data):
        with atomic():
            items = validated_data.pop("items")
            order = OrderModel.objects.create(
                user=self.context.get("request").user,
                **validated_data,
            )  # type: ignore
            for item in items:
                if item.variant.quantity < item.count:
                    raise serializers.ValidationError("Not enough quantity of product: {}".format(item.product.title))
                ItemModel.objects.create(
                    order=order,
                    product=item.product,
                    variant=item.variant,
                    count=item.count,
                    amount=item.variant.amount,
                    store=StoreModel.objects.filter(default=True).first(),
                )
                item.delete()
        if not validated_data.get("is_delivery"):
            confirm_order(order)
        return order

    class Meta(BaseOrderSerializer.Meta):
        fields = [
            "id",
            "items",
            "is_delivery",
            "address",
            "delivery_method",
        ]
