from django_filters import rest_framework as filters

from core.apps.payment.models import HistoryModel


class HistoryFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = HistoryModel
        fields = [
            "name",
        ]
