from django import forms

from core.apps.api.models import BasketModel, CategoryModel, ColorModel, ProductModel, SizeModel, TagModel


class ProductForm(forms.ModelForm):

    class Meta:
        model = ProductModel
        fields = "__all__"


class TagForm(forms.ModelForm):

    class Meta:
        model = TagModel
        fields = "__all__"


class CategoryForm(forms.ModelForm):

    class Meta:
        model = CategoryModel
        fields = "__all__"


class ColorForm(forms.ModelForm):

    class Meta:
        model = ColorModel
        fields = "__all__"


class SizeForm(forms.ModelForm):

    class Meta:
        model = SizeModel
        fields = "__all__"


class BasketForm(forms.ModelForm):

    class Meta:
        model = BasketModel
        fields = "__all__"
