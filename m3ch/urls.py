from django.urls import path, include
from . import views

app_name='m3ch'
urlpatterns = [
    path('top/', views.top, name='top'),

]