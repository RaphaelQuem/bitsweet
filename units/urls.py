from django.urls import path
from . import views

app_name='units'
urlpatterns= [
  path('',views.index,name='index'),
  path('create', views.create,name='create'),
  path('save', views.save,name='save'),
  path('<int:unit_id>/delete', views.delete,name='delete'),
]