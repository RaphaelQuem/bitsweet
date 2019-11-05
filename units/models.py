from django.db import models

class MeasurementUnit(models.Model):
    unit_id = models.AutoField(primary_key=True)
    unit_name = models.CharField(max_length=100, null=False)
    unit_abbreviation = models.CharField(max_length=10,null=True)
    
    def __str__(self):
        return self.unit_name