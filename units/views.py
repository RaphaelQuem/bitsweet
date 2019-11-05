from django.shortcuts import render
from ingredient.models import MeasurementUnit
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import UnitModelForm
import sys

def index(request):
    return render(request, 'units/index.html', {'unit_list': MeasurementUnit.objects.order_by('unit_id')})

def save(request):
    try:
        form = UnitModelForm(request.POST)
        if form.is_valid():
            formvalue = form.save(commit=False)

            unit = MeasurementUnit(
                                    unit_name= formvalue.unit_name,
                                    unit_abbreviation = formvalue.unit_abbreviation)
            unit.save()
    except:
        return render(request, 'units/create.html', {
            'form': form,
            'error_message': "Unexpected error: " + sys.exc_info()[0],
        })
    else:
        return HttpResponseRedirect(reverse('units:index', args=()))
    
def delete(request, unit_id):
    try:
        MeasurementUnit.objects.get(pk=unit_id).delete()
    except MeasurementUnit.DoesNotExist:
        render(
                request, 
                'units/index.html', 
                {
                    'unit_list': MeasurementUnit.objects.order_by('unit_id'),
                    'error_message': "Inexistent measurement unit!" 
                })
    
    return HttpResponseRedirect(reverse('units:index', args=()))



def create(request):
    unit =  MeasurementUnit()
    form = UnitModelForm(instance=unit)
    return render(request, 'units/create.html', 
                  {
                      'unit': unit,
                      'form': form
                  })

