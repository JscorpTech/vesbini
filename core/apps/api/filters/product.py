from django_filters import rest_framework as filters

from core.apps.api.models import BasketModel, CategoryModel, ColorModel, ProductModel, SizeModel, TagModel


class ProductFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = ProductModel
        fields = [
            "name",
        ]


class TagFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = TagModel
        fields = [
            "name",
        ]


class CategoryFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = CategoryModel
        fields = [
            "name",
        ]


class ColorFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = ColorModel
        fields = [
            "name",
        ]


class SizeFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = SizeModel
        fields = [
            "name",
        ]


class BasketFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = BasketModel
        fields = [
            "name",
        ]
