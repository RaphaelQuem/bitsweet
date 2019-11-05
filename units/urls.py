from django.urls import path
from . import views

app_name='units'
urlpatterns= [
  path('',views.index,name='index'),
  path('create', views.create,name='create'),
  path('save', views.save,name='save'),
 # path('<int:article_number>/del', views.delete,name='delete'),
]