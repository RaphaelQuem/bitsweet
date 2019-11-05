from django.shortcuts import render
from ingredient.models import MeasurementUnit

def index(request):
    return render(request, 'units/index.html', {'unit_list': MeasurementUnit.objects.order_by('unit_id')})

def save(request):
    return render(request, 'units/index.html', {'unit_list': MeasurementUnit.objects.order_by('unit_id')})

def create(request):
    unit =  MeasurementUnit()
    
    return render(request, 'units/create.html', 
                  {
                      'unit': unit
                  })

