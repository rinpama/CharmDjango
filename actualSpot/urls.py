from django.urls import path , include
from . import views

app_name='actualSpot'
urlpatterns = [
    path('spot',views.aspotList.as_view(),name='spotlist'),
    path('spot/<int:pk>/detail',views.actualSpotDetailView.as_view(),name='spotdetail'),
    path('spot/create/',views.actualSpotCreateView.as_view(),name='spotcreate'),
    path('spot/<int:pk>/update',views.actualSpotUpdateView.as_view(),name='spotupdate'),
    path('spot/<int:pk>/delete',views.actualSpotDeleteView.as_view(),name='spotdelete'),

    path('m',views.mostRecentList.as_view(),name='alist'),
    path('mostRecent/create/',views.mostRecentCreateView.as_view(),name='mostRecentcreate'),
    path('mostRecent/<int:pk>/update',views.mostRecentUpdateView.as_view(),name='mostRecentupdate'),
    path('mostRecent/<int:pk>/delete',views.mostRecentDeleteView.as_view(),name='mostRecentdelete'),

    path('g',views.gconList.as_view(),name='glist'),
    path('gcon/create/',views.gconCreateView.as_view(),name='gconcreate'),
    path('gcon/<int:pk>/update',views.gconUpdateView.as_view(),name='gconupdate'),
    path('gcon/<int:pk>/delete',views.gconDeleteView.as_view(),name='gcondelete'),
    
    path('vehicle',views.vehicleList.as_view(),name='vehiclelist'),
    path('vehicle/create/',views.vehicleCreateView.as_view(),name='vehiclecreate'),
    path('vehicle/<int:pk>/update',views.vehicleUpdateView.as_view(),name='vehicleupdate'),
    path('vehicle/<int:pk>/delete',views.vehicleDeleteView.as_view(),name='vehicledelete'),
]