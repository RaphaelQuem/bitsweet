from django.forms import ModelForm , TextInput, Textarea, NumberInput, Select
from .models import Recipe, IngredientInRecipe
 
class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        widgets = {
            'recipe_name': TextInput(attrs={'autofocus':'autofocus','placeholder': 'Recipe Name','class': 'form-control','style': 'font-size: 32px;'}),
            'recipe_img_url' : TextInput(attrs={'onchange':'updateImage()','id':'recipe_img_url_ip','placeholder': 'Paste the link to the recipe image :)', 'class':'form-control col-md-12'}),
            'recipe_description': Textarea(attrs={'placeholder': 'Example.: This recipe has been in my family for generations, my great grandmother used to boil eggs like this!', 'class':'form-control'}),
            'servings':NumberInput(attrs={'placeholder': 'Servings', 'class':'form-control text-center'}),
            'preparation_time':NumberInput(attrs={'placeholder': 'Time', 'class':'form-control text-center'})
        }
        fields = ['recipe_name','recipe_description', 'recipe_img_url', 'servings', 'preparation_time']
    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['recipe_img_url'].required = False
        
class IngredientInRecipeForm(ModelForm):
    class Meta:
        model = IngredientInRecipe
        widgets = {
            'amount_in_recipe':NumberInput(attrs={'placeholder': 'Amount', 'class':'form-control'}),
            'ingredient': Select(attrs={ 'class': 'form-control'})
        }
        fields = ['ingredient', 'amount_in_recipe']