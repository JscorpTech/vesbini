from modeltranslation.translator import TranslationOptions, register

from core.apps.accounts.models import CountryModel, RegionModel


@register(CountryModel)
class RegionTranslation(TranslationOptions):
    fields = ["name"]


@register(RegionModel)
class DistrictTranslation(TranslationOptions):
    fields = ["name"]
