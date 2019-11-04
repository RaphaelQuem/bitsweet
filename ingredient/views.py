from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q, ProtectedError
from .models import Ingredient, MeasurementUnit
from .forms import IngredientForm



def index(request):
    return render(request, 'ingredient/index.html', {'ingredient_list': Ingredient.objects.order_by('article_number')[:10]})

def filter(request):
    strfilter = request.POST['ingredient-filter']
    try:
        strfilter = int(strfilter)
        filtered =  Ingredient.objects.filter(
                Q(ingredient_name__icontains=strfilter) |
                Q(article_number__exact=strfilter)
            )[:10]
    except Exception:       
        filtered = Ingredient.objects.filter(ingredient_name__icontains=strfilter).order_by('article_number')[:10]

    return render(request, 'ingredient/index.html', {'ingredient_list': filtered, 'ingredient_filter': strfilter})

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
    try:
        Ingredient.objects.get(pk=article_number).delete()
    except ProtectedError:
        return render(request, 'ingredient/index.html', {
                'ingredient_list': Ingredient.objects.order_by('article_number')[:10],
                'error_message': 'tlt: this ingredient is currently being used :('
            })
    return HttpResponseRedirect(reverse('ingredient:index', args=()))

def save(request, article_number):
    try:
        form = IngredientForm(request.POST)
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