from django.urls import path, include
from . import views

app_name = 'Soen'
urlpatterns = [
    path('', views.Vindex, name='Vindex'),
    path('create/', views.Vcreate, name='Vcreate'),
    path('edit/<int:number>', views.Vedit, name='Vedit'),
    path('delete/<int:number>', views.Vdelete, name='Vdelete'),
    # path('detail/<int:pk>', views.IdModelDetail.as_view(), name='detail'),
    path('detail/<int:pk>', views.VIddetail, name='Vdetail'),
    path('main/', views.Vmain, name='Vmain'),
    path('sub/', views.Vsub, name='Vsub'),
]
