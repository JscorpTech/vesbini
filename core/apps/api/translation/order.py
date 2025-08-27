from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import ItemModel, OrderModel


@register(OrderModel)
class OrderTranslation(TranslationOptions):
    fields = []


@register(ItemModel)
class ItemTranslation(TranslationOptions):
    fields = []
