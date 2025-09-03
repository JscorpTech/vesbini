from django import forms

from core.apps.accounts.models import RegionModel, CountryModel


class RegionForm(forms.ModelForm):

    class Meta:
        model = CountryModel
        fields = "__all__"


class DistrictForm(forms.ModelForm):

    class Meta:
        model = RegionModel
        fields = "__all__"
