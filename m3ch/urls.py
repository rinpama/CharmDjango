from django.urls import path, include
from . import views

app_name='m3ch'
urlpatterns = [
    path('top/', views.top, name='top'),
    path('index/',views.index,name='index'),
    path('detail/<int:blog_id>/',views.detail,name='detail'),
    path('add_form',views.add_form,name='add_form'),

]