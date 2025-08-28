from django import forms

from core.apps.accounts.models import DistrictModel, RegionModel


class RegionForm(forms.ModelForm):

    class Meta:
        model = RegionModel
        fields = "__all__"


class DistrictForm(forms.ModelForm):

    class Meta:
        model = DistrictModel
        fields = "__all__"
