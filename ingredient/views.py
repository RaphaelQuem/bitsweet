from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Ingredient, MeasurementUnit
from .forms import IngredientForm


def index(request):
    return render(request, 'ingredient/index.html', {'ingredient_list': Ingredient.objects.order_by('article_number')[:10]})

def edit(request, article_number):
    try:
        ingredient = Ingredient.objects.get(pk=article_number)
    except Ingredient.DoesNotExist:
        ingredient = Ingredient()
    
    form = IngredientForm(instance=ingredient)
    return render(request, 'ingredient/edit.html', 
                    {'article_number': article_number,
                     'form':form })

def delete(request, article_number):
    Ingredient.objects.get(pk=article_number).delete()
    return HttpResponseRedirect(reverse('ingredient:index', args=()))

def save(request, article_number):
    try:
        form = IngredientForm(request.POST)
        print(form)
        if form.is_valid():
            formvalue = form.save(commit=False)
            if article_number != 0:
                ingredient = formvalue
                ingredient.article_number = article_number
            else:
                ingredient = Ingredient(
                                        ingredient_name= formvalue.ingredient_name,
                                        unit = formvalue.unit,
                                        cost_per_unit = formvalue.cost_per_unit,
                                        cost_amount = formvalue.cost_amount)
            ingredient.save()
    except Exception as e:
        return render(request, 'ingredient/edit.html', {
            'article_number': article_number,
            'form': form,
            'error_message': e,
        })
    else:
        return HttpResponseRedirect(reverse('ingredient:index', args=()))