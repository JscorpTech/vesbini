from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import StoreModel


@register(StoreModel)
class StoreTranslation(TranslationOptions):
    fields = []
