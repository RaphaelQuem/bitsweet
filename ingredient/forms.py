from django.forms import ModelForm ,NumberInput, TextInput, ChoiceField, Select
from .models import Ingredient, MeasurementUnit
 
class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        widgets = {
            'ingredient_name': TextInput(attrs={'autofocus':'autofocus','placeholder': 'Choose an intuitive name!', 'class': 'form-control'}),
            'cost_amount':NumberInput(attrs={'pattern':'0|[1-9]\d{0,2}','placeholder': 'Amount', 'class': 'form-control'}),
            'cost_per_unit':NumberInput(attrs={'placeholder': 'Cost', 'class': 'form-control'}),
            'unit': Select(attrs={ 'class': 'form-control'})
        }
        fields = ['ingredient_name','cost_per_unit','cost_amount', 'unit']