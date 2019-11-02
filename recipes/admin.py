from django.contrib import admin
from .models import Recipe, IngredientInRecipe

admin.site.register(Recipe)
admin.site.register(IngredientInRecipe)