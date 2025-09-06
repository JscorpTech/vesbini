from django.contrib import admin
from django.db import models
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin, TabularInline
from unfold.contrib.filters.admin import (
    FieldTextFilter,
    MultipleRelatedDropdownFilter,
)
from unfold.contrib.forms.widgets import WysiwygWidget

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
class ProductAdmin(TabbedTranslationAdmin, ModelAdmin):
    inlines = [ProductVariantInline]
    list_filter_submit = True
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }
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
class TagAdmin(TabbedTranslationAdmin, ModelAdmin):
    search_fields = ["name"]
    list_display = (
        "id",
        "__str__",
    )


@admin.register(CategoryModel)
class CategoryAdmin(TabbedTranslationAdmin, ModelAdmin):
    search_fields = ["name"]
    list_display = (
        "id",
        "__str__",
    )


@admin.register(ColorModel)
class ColorAdmin(TabbedTranslationAdmin, ModelAdmin):
    search_fields = ["name"]
    list_display = (
        "id",
        "__str__",
    )


@admin.register(SizeModel)
class SizeAdmin(TabbedTranslationAdmin, ModelAdmin):
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
