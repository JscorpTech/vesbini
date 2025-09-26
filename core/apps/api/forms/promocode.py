from django import forms

from core.apps.api.models import PromocodeModel


class PromocodeForm(forms.ModelForm):

    class Meta:
        model = PromocodeModel
        fields = "__all__"
