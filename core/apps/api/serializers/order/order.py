from django.db.transaction import atomic
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.apps.accounts.services.balance import subtract_balance
from core.apps.api.models import OrderModel
from core.apps.api.models.moysklad import StoreModel
from core.apps.api.models.order import ItemModel
from core.apps.api.models.product import BasketModel
from core.apps.api.models.promocode import PromocodeModel
from core.apps.api.serializers.delivery.deliverymethod import ListDeliveryMethodSerializer
from core.apps.api.serializers.order.item import ListItemSerializer
from core.apps.api.services.order import calc_promocode_discount, confirm_order
from core.services.promocode import subtract_promocode, validate_promocode


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
    delivery_method = ListDeliveryMethodSerializer()

    class Meta(BaseOrderSerializer.Meta): ...


class RetrieveOrderSerializer(BaseOrderSerializer):
    delivery_method = ListDeliveryMethodSerializer()

    class Meta(BaseOrderSerializer.Meta): ...


class CreateOrderSerializer(BaseOrderSerializer):
    items = serializers.ListField(
        child=serializers.PrimaryKeyRelatedField(queryset=BasketModel.objects.all()), write_only=True
    )
    promocode = serializers.CharField(write_only=True, required=False)

    def validate_promocode(self, value):
        if not validate_promocode(value):
            raise serializers.ValidationError(detail=_("Promocode invalid"))
        obj = PromocodeModel.objects.filter(code=value).first()
        if obj is None:
            raise serializers.ValidationError(detail=_("promocode invalid"))
        return obj

    def validate_use_cashback(self, value):
        if int(value) > self.context.get("request").user.profile.balance:
            raise serializers.ValidationError(detail=_("Not enough cashback"))
        return value

    def validate(self, attrs):
        if attrs.get("is_delivery", False):
            if attrs.get("delivery_method") is None:
                raise serializers.ValidationError({"delivery_method": [_("Delivery method field is required")]})
        return attrs

    def to_representation(self, instance):
        return {"id": instance.id}

    def create(self, validated_data):
        request = self.context.get("request")
        if request is None:
            raise ValidationError("request is None")
        with atomic():
            items = validated_data.pop("items")
            order = OrderModel.objects.create(
                user=request.user,
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
            order.promocode_discount = calc_promocode_discount(order.amount, order.promocode)
            subtract_promocode(order.promocode)
            subtract_balance(order.user, order.use_cashback)
            order.save()
        if not validated_data.get("is_delivery"):
            confirm_order(order, False)
        return order

    class Meta(BaseOrderSerializer.Meta):
        fields = [
            "id",
            "items",
            "promocode",
            "promocode_discount",
            "use_cashback",
            "is_delivery",
            "address",
            "delivery_method",
        ]
