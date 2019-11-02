from django.forms import ModelForm , TextInput
from .models import Recipe
 
class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipe_name','recipe_description', 'recipe_img_url']