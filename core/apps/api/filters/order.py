from django_filters import rest_framework as filters

from core.apps.api.models import ItemModel, OrderModel


class OrderFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = OrderModel
        fields = [
            "name",
        ]


class ItemFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = ItemModel
        fields = [
            "name",
        ]
