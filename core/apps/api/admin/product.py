from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from unfold.contrib.filters.admin import (
    FieldTextFilter,
    MultipleRelatedDropdownFilter,
)

from core.apps.api.models import BasketModel, CategoryModel, ColorModel, ProductModel, SizeModel, TagModel
from core.apps.api.models.product import ProductVariantModel


class ProductVariantInline(TabularInline):
    model = ProductVariantModel
    tab = True
    extra = 0
    can_delete = False

    def get_readonly_fields(self, request, obj=...):
        return ["product", "color", "size"]

    def has_add_permission(self, request, obj) -> bool:
        return False


@admin.register(ProductModel)
class ProductAdmin(ModelAdmin):
    inlines = [ProductVariantInline]
    list_filter_submit = True
    list_filter = [
        ("title", FieldTextFilter),
        ("variants__sku", FieldTextFilter),
        ("desc", FieldTextFilter),
        ("categories", MultipleRelatedDropdownFilter),
        ("tags", MultipleRelatedDropdownFilter),
        ("colors", MultipleRelatedDropdownFilter),
        ("sizes", MultipleRelatedDropdownFilter),
    ]
    autocomplete_fields = [
        "colors",
        "sizes",
        "tags",
        "categories",
    ]
    list_display = (
        "id",
        "__str__",
    )


@admin.register(TagModel)
class TagAdmin(ModelAdmin):
    search_fields = ["name"]
    list_display = (
        "id",
        "__str__",
    )


@admin.register(CategoryModel)
class CategoryAdmin(ModelAdmin):
    search_fields = ["name"]
    list_display = (
        "id",
        "__str__",
    )


@admin.register(ColorModel)
class ColorAdmin(ModelAdmin):
    search_fields = ["name"]
    list_display = (
        "id",
        "__str__",
    )


@admin.register(SizeModel)
class SizeAdmin(ModelAdmin):
    search_fields = ["name"]
    list_display = (
        "id",
        "__str__",
    )


@admin.register(BasketModel)
class BasketAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
