from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import BasketModel, CategoryModel, ColorModel, ProductModel, SizeModel, TagModel


@register(ProductModel)
class ProductTranslation(TranslationOptions):
    fields = []


@register(TagModel)
class TagTranslation(TranslationOptions):
    fields = []


@register(CategoryModel)
class CategoryTranslation(TranslationOptions):
    fields = []


@register(ColorModel)
class ColorTranslation(TranslationOptions):
    fields = []


@register(SizeModel)
class SizeTranslation(TranslationOptions):
    fields = []


@register(BasketModel)
class BasketTranslation(TranslationOptions):
    fields = []
