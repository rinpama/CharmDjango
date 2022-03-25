from django.urls import path , include
from . import views

app_name='reimex'
urlpatterns = [
    path('top',views.top,name='top'),
    path('m',views.SoenMemberList.as_view(),name='mlist'),

    # path('',views.SoenModelList.as_view(),name='slist'),
    path('detail/<int:pk>/',views.SoenModelDetail.as_view(),name='sdetail'),
    path('create/',views.SoenModelCreate.as_view(),name='screate'),
    path('<int:pk>/update/',views.SoenModelUpdate.as_view(),name='supdate'),
    path('<int:pk>/delete/',views.SoenModelDelete.as_view(),name='sdelete'),

    path('testprint',views.testprint,name='testdo'),
    path('aspot',views.aspot,name='aspot'),
    
    path('memFalse',views.memFalse,name='memFalse'),
    path('onlymemFalse',views.onlymemFalse,name='onlymemFalse'),
    path('spotFalse',views.spotFalse,name='spotFalse'),

    
]