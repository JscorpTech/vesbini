from modeltranslation.translator import TranslationOptions, register

from core.apps.accounts.models import RegionModel, CountryModel


@register(CountryModel)
class RegionTranslation(TranslationOptions):
    fields = []


@register(RegionModel)
class DistrictTranslation(TranslationOptions):
    fields = []
