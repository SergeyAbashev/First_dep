from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'discount', 'preview']


class CSVImportForm(forms.Form):
    csv_file = forms.FileField()
    