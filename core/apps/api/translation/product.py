from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import BasketModel, CategoryModel, ColorModel, ProductModel, SizeModel, TagModel


@register(ProductModel)
class ProductTranslation(TranslationOptions):
    fields = ["title", "desc"]


@register(TagModel)
class TagTranslation(TranslationOptions):
    fields = ["name"]


@register(CategoryModel)
class CategoryTranslation(TranslationOptions):
    fields = ["name"]


@register(ColorModel)
class ColorTranslation(TranslationOptions):
    fields = ["name"]


@register(SizeModel)
class SizeTranslation(TranslationOptions):
    fields = ["name"]


@register(BasketModel)
class BasketTranslation(TranslationOptions):
    fields = []
