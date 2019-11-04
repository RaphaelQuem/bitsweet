from django.shortcuts import render
from .models import Recipe, IngredientInRecipe
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from ingredient.models import Ingredient
from django.urls import reverse
from .forms import RecipeForm, IngredientInRecipeForm
from django.core import serializers
from django.db.models import F, Sum
from django.db.utils import IntegrityError
import sys


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
                
    except:
        context = get_recipe_context(recipe_id,False)
        context["error_message"] = "tlt:Unexpected error" + sys.exc_info()[0]
        return render(
            request, 
            'recipes/details.html', 
            context)
    else:
        return HttpResponseRedirect(reverse('recipes:edit', args=[recipe.recipe_id]))
    
def delete(request, recipe_id):
    try:
        Recipe.objects.get(pk=recipe_id).delete()
    except Recipe.DoesNotExist:
        render(
                request, 
                'recipes/index.html', 
                {
                    'recipe_list': Recipe.objects.order_by('recipe_id')[:10],
                    'error_message': "tlt:Recipe does not exist" 
                })
    
    return HttpResponseRedirect(reverse('recipes:index', args=()))

def del_ingredient(request, recipe_ingredient_id):
    ing_rec = IngredientInRecipe.objects.get(pk=recipe_ingredient_id)
    recipe_id = ing_rec.recipe.recipe_id
    recipe = Recipe.objects.get(pk=recipe_id)
    ing_rec.delete()
    recipe.save()
    return HttpResponseRedirect(reverse('recipes:edit', args=[recipe.recipe_id]))

def add_ingredient(request, recipe_id):
    recipe = get_recipe(recipe_id)
    try:
        ing_rec_form = IngredientInRecipeForm(request.POST)
        formvalue = ing_rec_form.save(commit=False)
        
        ing_rec = IngredientInRecipe()
        ing_rec.recipe = recipe
        ing_rec.ingredient = formvalue.ingredient
        ing_rec.amount_in_recipe = formvalue.amount_in_recipe
        ing_rec.cost = (ing_rec.amount_in_recipe * ing_rec.ingredient.cost_per_unit) / ing_rec.ingredient.cost_amount
        ing_rec.save()
        
        recipe.recipe_ingredients.add(ing_rec)
        recipe.save()
        
    except IntegrityError:
        context = get_recipe_context(recipe_id, False)
        context["error_message"] = "tlt: save the recipe first"
        return render(
                request, 
                'recipes/detail.html',
                context
                )
    except:
        context = get_recipe_context(recipe_id, False)
        context["error_message"] = "tlt:Unexpected error" + sys.exc_info()[0]
        return render(
                request, 
                'recipes/detail.html',
                context
                )
        
    return HttpResponseRedirect(reverse('recipes:edit', args=[recipe.recipe_id]))
    
    
def details(request, recipe_id):
    return render(
        request,
        'recipes/detail.html',
        get_recipe_context(recipe_id, True) 
    )

def edit(request, recipe_id):
    return render(
        request,
        'recipes/detail.html',
        get_recipe_context(recipe_id, False) 
    )
    
def get_recipe(recipe_id):
    try:
        recipe = Recipe.objects.get(pk=recipe_id)
    except Recipe.DoesNotExist:
        recipe = Recipe()
        recipe.recipe_id = recipe_id
    
    return recipe
    
def get_recipe_context(recipe_id, readonly):
    recipe = get_recipe(recipe_id)
    form = RecipeForm(instance=recipe)
    
    ing_rec = IngredientInRecipe()
    ing_rec.recipe = recipe
    ing_rec_form = IngredientInRecipeForm(instance=ing_rec)
    
    aggr = recipe.recipe_ingredients.aggregate(
            total_cost=Sum(F('cost'))
        )
    
    return {
        'recipe': recipe,
        'form':form,
        'ing_rec_form': ing_rec_form,
        'readonly': readonly,
        'recipe_cost': aggr['total_cost']
    }
    
