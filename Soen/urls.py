from django.urls import path, include
from . import views

app_name = 'Soen'
urlpatterns = [
    path('', views.Vindex, name='Vindex'),#SoenMemberList(簡易)
    path('detail/<int:number>/', views.Vdetail, name='Vdetail'),
    path('create/', views.Vcreate, name='Vcreate'),

    path('logmain/', views.Vlogmain, name='Vlogmain'),
    path('logmainsub/', views.Vlogmainsub, name='Vlogmainsub'),
    path('logsmemlist/', views.Vlogsmemlist, name='Vlogsmemlist'),
    path('logsmemdetail/<int:number>/', views.Vlogsmemdetail, name='Vlogsmemdetail'),
    path('logsmemcreatemore/', views.Vlogsmemcreatemore, name='Vlogsmemcreatemore'),
    path('logsmemedit/<int:number>/', views.Vlogsmemedit, name='Vlogsmemedit'),
    path('logsmemdelete/<int:number>/', views.Vlogsmemdelete, name='Vlogsmemdelete'),

]
