from django import forms
from .models import Persons

class PersonsForm(forms.ModelForm):
    class Meta:
        model = Persons
        fields = ["name","message",]