from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import DeliveryMethodModel


@register(DeliveryMethodModel)
class DeliverymethodTranslation(TranslationOptions):
    fields = ["name"]
