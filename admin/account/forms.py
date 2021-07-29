from django import forms
from .models import Category, UsersInfo, Cards


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class UsersInfoForm(forms.ModelForm):
    class Meta:
        model = UsersInfo
        fields = '__all__'


class CardsForm(forms.ModelForm):
    class Meta:
        model = Cards
        fields = '__all__'
