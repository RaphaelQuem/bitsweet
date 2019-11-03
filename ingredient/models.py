from django.db import models
from django.core.validators import  MinValueValidator

class MeasurementUnit(models.Model):
    unit_id = models.AutoField(primary_key=True)
    unit_name = models.CharField(max_length=100, null=False)
    unit_abbreviation = models.CharField(max_length=10,null=True)
    
    def __str__(self):
        return self.unit_name

class Ingredient(models.Model):
    article_number = models.AutoField(primary_key=True)
    ingredient_name = models.CharField(max_length=100, null=False)
    cost_amount = models.FloatField(validators=[MinValueValidator(0.1)])
    cost_per_unit = models.FloatField(validators=[MinValueValidator(0)])
    unit = models.ForeignKey(MeasurementUnit,on_delete=models.CASCADE)

    def __str__(self):
        return self.ingredient_name