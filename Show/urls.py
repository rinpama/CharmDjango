from django.urls import path, include
from . import views

app_name = 'Show'
urlpatterns = [
    path('sekoList', views.VsekoList, name='VsekoList'),
    path('sekoListSearch', views.VsekoListSearch, name='VsekoListSearch'),
    path('seko', views.Vsekotai, name='Vsekotai'),  # create
    path('sekodetail/<int:pk>', views.Vsekodetail, name='Vsekodetail'),  # create
    path('nweseko', views.Vnewsekotai, name='Vnewsekotai'),  # newcreate
    path('sekoedit/<int:pk>', views.Vsekoedit, name='Vsekoedit'),
    path('sekodelete/<int:pk>', views.Vsekodelete, name='Vsekodelete'),
]
