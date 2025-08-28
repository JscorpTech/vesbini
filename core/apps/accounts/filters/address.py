from django_filters import rest_framework as filters

from core.apps.accounts.models import DistrictModel, RegionModel


class RegionFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = RegionModel
        fields = [
            "name",
        ]


class DistrictFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = DistrictModel
        fields = [
            "name",
        ]
