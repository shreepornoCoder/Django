from django import forms
from .models import Category

class CategoryrForms(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
