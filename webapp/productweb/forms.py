# forms.py
from django import forms
from .models import Item, ItemImage

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'size', 'description', 'material', 'price']

class ItemImageForm(forms.ModelForm):
    class Meta:
        model = ItemImage
        fields = ['image']

class YourCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1, widget=forms.NumberInput(attrs={'class': 'form-control'}))