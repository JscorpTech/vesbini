from django import forms

from core.apps.payment.models import HistoryModel


class HistoryForm(forms.ModelForm):

    class Meta:
        model = HistoryModel
        fields = "__all__"
