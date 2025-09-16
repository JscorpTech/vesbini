from core.apps.bot.models import Messages
from modeltranslation.translator import TranslationOptions, register


@register(Messages)
class MessageTranslation(TranslationOptions):
    fields = ["value"]
