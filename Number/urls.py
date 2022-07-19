from django.urls import path, include
from .views import *

app_name = 'Number'
urlpatterns = [
    path('', topView, name='topView'),
path('inputWages', InputWages, name='inputWages'),
    path('inputSteelP', InputSteelParts, name='inputSteelP'),
    path('listPartsList', ListPartsList, name='listPartsList'),
    path('listSteelParts/<int:number>/', ListSteelParts, name='listSteelParts'),

# path('makeEstimatedUnitprice', makeEstimatedUnitprice, name='makeEstimatedUnitprice'),
]
