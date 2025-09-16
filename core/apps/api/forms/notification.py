from django import forms

from core.apps.api.models import NotificationModel, UserNotificationModel


class NotificationForm(forms.ModelForm):

    class Meta:
        model = NotificationModel
        fields = "__all__"


class UsernotificationForm(forms.ModelForm):

    class Meta:
        model = UserNotificationModel
        fields = "__all__"
