from django import forms
from .models import Pelerin

class PelerinForm(forms.ModelForm):
    class Meta:
        model = Pelerin
        fields = "__all__"
