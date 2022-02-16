from django.urls import path, include
from . import views

app_name = 'mydjangoSoen'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('edit/<int:number>', views.edit, name='edit'),
    path('delete/<int:number>', views.delete, name='delete'),
    path('detail/<int:pk>', views.IdModelDetail.as_view(), name='detail'),
    path('main/', views.main, name='main'),
    path('sub/', views.sub, name='sub'),
]
