from django import forms

from core.apps.api.models import ItemModel, OrderModel


class OrderForm(forms.ModelForm):

    class Meta:
        model = OrderModel
        fields = "__all__"


class ItemForm(forms.ModelForm):

    class Meta:
        model = ItemModel
        fields = "__all__"
