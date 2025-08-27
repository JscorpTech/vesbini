from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline

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
    autocomplete_fields = [
        "colors",
        "sizes",
    ]
    list_display = (
        "id",
        "__str__",
    )


@admin.register(TagModel)
class TagAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(CategoryModel)
class CategoryAdmin(ModelAdmin):
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
