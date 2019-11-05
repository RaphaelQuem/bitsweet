from django.urls import path
from . import views

app_name='ingredient'
urlpatterns= [
  path('',views.index,name='index'),
  path('<int:article_number>/edit', views.edit,name='edit'),
  path('<int:article_number>/save', views.save,name='save'),
  path('<int:article_number>/del', views.delete,name='delete'),
  path('filter', views.filter,name='filter'),
]



