from django.forms import ModelForm ,NumberInput, TextInput, ChoiceField, Select
from .models import MeasurementUnit
 
class UnitModelForm(ModelForm):
    class Meta:
        model = MeasurementUnit
        widgets = {
            'unit_name': TextInput(attrs={'autofocus':'autofocus','placeholder': 'Unit name', 'class': 'form-control'}),
            'unit_abbreviation': TextInput(attrs={'autofocus':'autofocus','placeholder': 'Abbreviation', 'class': 'form-control'}),
        }
        fields = ['unit_name','unit_abbreviation']