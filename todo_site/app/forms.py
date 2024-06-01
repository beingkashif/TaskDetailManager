from .models import app
from django import forms

class appForm(forms.ModelForm):
    class Meta:
        model = app
        fields = '__all__'
