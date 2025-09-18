from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import FeedbackModel


@register(FeedbackModel)
class FeedbackTranslation(TranslationOptions):
    fields = []
