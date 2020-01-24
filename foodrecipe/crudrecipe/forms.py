from django import forms
from .models import Cookbook

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Cookbook
        fields = ('title', 'username', 'pdf')
        