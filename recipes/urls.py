from django.urls import path
from . import views

app_name='recipes'
urlpatterns= [
  path('',views.index,name='index'),
  path('<int:recipe_id>/edit',views.edit,name='edit'),
  path('<int:recipe_id>',views.add_ingredient,name='add_ingredient')
]