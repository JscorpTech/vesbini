from django import forms

from core.apps.api.models import FeedbackModel


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = FeedbackModel
        fields = "__all__"
