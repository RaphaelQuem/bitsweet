from django.forms import ModelForm ,NumberInput, TextInput, ChoiceField, Select
from ingredient.models import Ingredient, MeasurementUnit
 
class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        labels = {
            'unit': 'aaaaaaa'
        }
        widgets = {
            'ingredient_name': TextInput(attrs={'placeholder': 'AAAA','style':'width:100px;'}),
            'unit': Select(attrs={'style': 'color:red;'})
        }
        fields = ['ingredient_name','cost_per_unit', 'unit']