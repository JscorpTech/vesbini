from django_filters import rest_framework as filters

from core.apps.accounts.models import CountryModel, RegionModel


class RegionFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = CountryModel
        fields = [
            "name",
        ]


class DistrictFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = RegionModel
        fields = [
            "name",
        ]
