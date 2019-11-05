from django.db import models
from django.core.validators import  MinValueValidator
from units.models import MeasurementUnit


class Ingredient(models.Model):
    article_number = models.AutoField(primary_key=True)
    ingredient_name = models.CharField(max_length=100, null=False)
    cost_amount = models.FloatField(validators=[MinValueValidator(0.1)])
    cost_per_unit = models.FloatField(validators=[MinValueValidator(0)])
    unit = models.ForeignKey(MeasurementUnit,on_delete=models.CASCADE)

    def __str__(self):
        return self.ingredient_name