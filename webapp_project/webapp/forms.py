from django import forms
from . models import App

class App_Form(forms.ModelForm):
    class Meta:
        model = App
        fields = ['name', 'description', 'year', 'image']