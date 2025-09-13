from django import forms

from core.apps.api.models import DeliveryMethodModel


class DeliverymethodForm(forms.ModelForm):

    class Meta:
        model = DeliveryMethodModel
        fields = "__all__"
