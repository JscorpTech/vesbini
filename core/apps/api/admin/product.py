from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin, TabularInline
from unfold.contrib.filters.admin import (
    BooleanRadioFilter,
    FieldTextFilter,
    MultipleRelatedDropdownFilter,
)
from unfold.contrib.forms.widgets import WysiwygWidget
from unfold.decorators import display

from core.apps.api.models import BasketModel, CategoryModel, ColorModel, ProductModel, SizeModel, TagModel
from core.apps.api.models.product import ProductImageModel, ProductVariantModel


class ProductImageInline(TabularInline):
    model = ProductImageModel
    tab = True
    extra = 1
    autocomplete_fields = ["color"]


class ProductVariantInline(TabularInline):
    model = ProductVariantModel
    tab = True
    extra = 0
    can_delete = False
    fields = ["color", "size", "quantity", "amount", "sku", "is_bundle" "updated_at"]

    def get_readonly_fields(self, request, obj=...):
        return ["product", "color", "size", "updated_at", "href"]

    def has_add_permission(self, request, obj) -> bool:
        return False


@admin.register(ProductModel)
class ProductAdmin(TabbedTranslationAdmin, ModelAdmin):
    inlines = [ProductVariantInline, ProductImageInline]
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
        ("status", BooleanRadioFilter),
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
        "title",
        "_amount",
        "_status",
        "created_at",
    )

    @display(description=_("status"), boolean=True)
    def _status(self, obj):
        return obj.status

    @display(description=_("amount"), label=True)
    def _amount(self, obj):
        return "{:,.2f} so'm".format(obj.amount)


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
