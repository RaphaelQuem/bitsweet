from django.shortcuts import render
from .models import Recipe, IngredientInRecipe
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from ingredient.models import Ingredient
from django.urls import reverse
from .forms import RecipeForm, IngredientInRecipeForm
from django.core import serializers


def index(request):
    return render(request, 'recipes/index.html', {'recipe_list': Recipe.objects.order_by('recipe_id')[:10]})

def save(request, recipe_id):
    try:
        form = RecipeForm(request.POST)
        if form.is_valid():
            formvalue = form.save(commit=False)
            if recipe_id != 0:
                recipe = formvalue
                recipe.recipe_id = recipe_id
            else:
                recipe = Recipe(
                                        recipe_name= formvalue.recipe_name,
                                        recipe_description = formvalue.recipe_description,
                                        recipe_img_url = formvalue.recipe_img_url,
                                        servings = formvalue.servings,
                                        preparation_time = formvalue.preparation_time)
            recipe.save()
    except Exception as e:
        context = get_recipe_context(recipe_id)
        context['error_message'] = e
        return render(
            request, 
            'recipes/details.html', 
            context)
    else:
        return HttpResponseRedirect(reverse('recipes:index', args=()))

def del_ingredient(request, recipe_ingredient_id):
    print('del_ingredient')
    ing_rec = IngredientInRecipe.objects.get(pk=recipe_ingredient_id)
    recipe_id = ing_rec.recipe.recipe_id
    recipe = Recipe.objects.get(pk=recipe_id)
    ing_rec.delete()
    recipe.save()
    return render(
        request,
        'recipes/detail.html',
        get_recipe_context(recipe_id) 
    )

def add_ingredient(request, recipe_id):
    recipe = get_recipe(recipe_id)
    try:
        ing_rec_form = IngredientInRecipeForm(request.POST)
        formvalue = ing_rec_form.save(commit=False)
        
        ing_rec = IngredientInRecipe()
        ing_rec.recipe = recipe
        ing_rec.ingredient = formvalue.ingredient
        ing_rec.amount_in_recipe = formvalue.amount_in_recipe
        ing_rec.save()
        
        recipe.recipe_ingredients.add(ing_rec)
        recipe.save()
        
    except Exception as e:
        return render(
                request, 
                'recipes/detail.html',
                { 'e': e})
        
    #redirect?
    return render(
        request,
        'recipes/detail.html',
        get_recipe_context(recipe_id)
    )

def edit(request, recipe_id):
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
        recipe.recipe_id = recipe_id
    
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
    
