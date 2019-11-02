from django.forms import ModelForm , TextInput
from .models import Recipe, IngredientInRecipe
 
class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipe_name','recipe_description', 'recipe_img_url']
        
class IngredientInRecipeForm(ModelForm):
    class Meta:
        model = IngredientInRecipe
        fields = ['ingredient', 'amount_in_recipe']