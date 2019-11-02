from django.db import models
from ingredient.models import Ingredient

class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    recipe_name = models.CharField(max_length=100, null=False)
    recipe_description = models.TextField(null=False)
    #ingredients = models.ManyToManyField(Ingredient, through='IngredientInRecipe')
    recipe_img_url = models.CharField(max_length=300, null=True)
    def __str__(self):
        return self.recipe_name
    
class IngredientInRecipe(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    recipe = models.ForeignKey(Recipe, on_delete=models.PROTECT, related_name="recipe_ingredients")
    amount_in_recipe = models.IntegerField()
