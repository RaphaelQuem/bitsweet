from django.shortcuts import render
from .models import Recipe

def index(request):
    return render(request, 'recipes/index.html', {'recipe_list': Recipe.objects.order_by('recipe_id')[:10]})
