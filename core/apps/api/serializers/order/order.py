from django.db.transaction import atomic
from rest_framework import serializers

from core.apps.api.models import OrderModel
from core.apps.api.models.moysklad import StoreModel
from core.apps.api.models.order import ItemModel
from core.apps.api.models.product import BasketModel
from core.apps.api.serializers.order.item import ListItemSerializer


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
        ]


class ListOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta): ...


class RetrieveOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta): ...


class CreateOrderSerializer(BaseOrderSerializer):
    items = serializers.ListField(
        child=serializers.PrimaryKeyRelatedField(queryset=BasketModel.objects.all()), write_only=True
    )

    def to_representation(self, instance):
        return {"id": instance.id}

    def create(self, validated_data):
        with atomic():
            order = OrderModel.objects.create(user=self.context.get("request").user)  # type: ignore
            for item in validated_data.get("items"):
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
        return order

    class Meta(BaseOrderSerializer.Meta):
        fields = [
            "id",
            "items",
        ]
