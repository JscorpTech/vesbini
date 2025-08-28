from modeltranslation.translator import TranslationOptions, register

from core.apps.accounts.models import DistrictModel, RegionModel


@register(RegionModel)
class RegionTranslation(TranslationOptions):
    fields = []


@register(DistrictModel)
class DistrictTranslation(TranslationOptions):
    fields = []
