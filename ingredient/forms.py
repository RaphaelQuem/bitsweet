from django.forms import ModelForm ,NumberInput, TextInput, ChoiceField, Select
from ingredient.models import Ingredient, MeasurementUnit
 
class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        widgets = {
            'ingredient_name': TextInput(attrs={'placeholder': 'tlt:Ingredient Name'}),
            'cost_amount':TextInput(attrs={'placeholder': 'tlt:Amount'}),
            'cost_per_unit':TextInput(attrs={'placeholder': 'tlt:Cost'}),
            'unit': Select()
        }
        fields = ['ingredient_name','cost_per_unit','cost_amount', 'unit']