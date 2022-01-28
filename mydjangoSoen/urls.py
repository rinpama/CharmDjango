from django.urls import path, include
from . import views

app_name = 'mydjangoSoen'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('edit/<int:number>', views.edit, name='edit'),
    path('delete/<int:number>', views.delete, name='delete'),
    path('find/',views.find,name='find'),
    path('main/', views.main, name='main'),
    path('sub/', views.sub, name='sub'),
]
