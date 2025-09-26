from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import PromocodeModel


@register(PromocodeModel)
class PromocodeTranslation(TranslationOptions):
    fields = []
