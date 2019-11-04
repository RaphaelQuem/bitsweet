from django.forms import ModelForm , TextInput, Textarea, NumberInput
from .models import Recipe, IngredientInRecipe
 
class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        widgets = {
            'recipe_name': TextInput(attrs={'placeholder': 'tlt:Recipe Name', 'class': 'form-control','style': 'font-size: 32px;'}),
            'recipe_img_url' : TextInput(attrs={'placeholder': 'tlt:Recipe_img_url', 'class':'form-control col-md-12'}),
            'recipe_description': Textarea(attrs={'placeholder': 'tlt:Describe', 'class':'form-control'}),
            'servings':NumberInput(attrs={'placeholder': 'tlt:Servings', 'class':'form-control','pattern':'[0-9]+'}),
            'preparation_time':NumberInput(attrs={'placeholder': 'tlt:Servings', 'class':'form-control'})
        }
        fields = ['recipe_name','recipe_description', 'recipe_img_url', 'servings', 'preparation_time']
    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['recipe_img_url'].required = False
        
class IngredientInRecipeForm(ModelForm):
    class Meta:
        model = IngredientInRecipe
        fields = ['ingredient', 'amount_in_recipe']