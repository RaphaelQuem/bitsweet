from django.shortcuts import render
from .models import Recipe, IngredientInRecipe
from .forms import RecipeForm, IngredientInRecipeForm

def index(request):
    return render(request, 'recipes/index.html', {'recipe_list': Recipe.objects.order_by('recipe_id')[:10]})

def add_ingredient(request, recipe_id):
    recipe = get_recipe(recipe_id)
    try:
        print('try')
        ing_rec_form = IngredientInRecipeForm(request.POST)
        formvalue = ing_rec_form.save(commit=False)
        
        ing_rec = IngredientInRecipe()
        ing_rec.recipe = recipe
        ing_rec.ingredient = formvalue.ingredient
        ing_rec.amount_in_recipe = formvalue.amount_in_recipe
        ing_rec.save()
        
        recipe.recipe_ingredients.add(ing_rec)
        recipe.save()
        
        print('ing_rec_form', ing_rec_form)
        print('ing_rec', ing_rec)
        print('formvalue', formvalue)
        print('recipe', recipe)
    except Exception as e:
        print(e)
        return render(request, 'ingredient/edit.html', { 'e': e})
        
    #redirect?
    return render(
        request,
        'recipes/detail.html',
        get_recipe_context(recipe_id)
    )

def edit(request, recipe_id):
    print('edit')
    return render(
        request,
        'recipes/detail.html',
        get_recipe_context(recipe_id) 
    )
    
def get_recipe(recipe_id):
    try:
        recipe = Recipe.objects.get(pk=recipe_id)
    except Recipe.DoesNotExist:
        recipe = Recipe()
    
    return recipe
    
def get_recipe_context(recipe_id):
    recipe = get_recipe(recipe_id)
    form = RecipeForm(instance=recipe)
    
    ing_rec = IngredientInRecipe()
    ing_rec.recipe = recipe
    ing_rec_form = IngredientInRecipeForm(instance=ing_rec)
    
    return {
        'recipe': recipe,
        'form':form,
        'ing_rec_form': ing_rec_form
    }
    
