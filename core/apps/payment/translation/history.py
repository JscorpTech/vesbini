from modeltranslation.translator import TranslationOptions, register

from core.apps.payment.models import HistoryModel


@register(HistoryModel)
class HistoryTranslation(TranslationOptions):
    fields = []
