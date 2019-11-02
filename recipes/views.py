from django.shortcuts import render
from django.core import serializers
from .models import Recipe
from .forms import RecipeForm

def index(request):
    return render(request, 'recipes/index.html', {'recipe_list': Recipe.objects.order_by('recipe_id')[:10]})

def edit(request, recipe_id):
    try:
        recipe = Recipe.objects.get(pk=recipe_id)
    except Recipe.DoesNotExist:
        recipe = Recipe()
        
    data = serializers.serialize("json", [recipe])
    
    form = RecipeForm(instance=recipe)
    return render(request, 'recipes/detail.html', 
                    {'recipe': recipe,
                     'form':form,
                     'data':data}
                      
                    )

