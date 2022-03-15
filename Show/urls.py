from django.urls import path, include
from . import views

app_name = 'Show'
urlpatterns = [
    path('sekoList', views.VsekoList, name='VsekoList'),
    path('sekoListSearch', views.VsekoListSearch, name='VsekoListSearch'),
    path('sekodetail/<int:number>', views.Vsekodetail, name='Vsekodetail'),
    path('sekocreate/', views.Vsekocreate, name='Vsekocreate'),

    path('logsekoList', views.VlogsekoList, name='VlogsekoList'),
    path('logsekocreate/', views.Vlogsekocreate, name='Vlogsekocreate'),
    path('logsekosmemcreate', views.Vlogsekosmemcreate, name='Vlogsekosmemcreate'),
    path('logsekosmemlist', views.Vlogsekosmemlist, name='Vlogsekosmemlist'),
    path('logsekoedit/<int:number>', views.Vlogsekoedit, name='Vlogsekoedit'),
    path('logsekodelete/<int:number>', views.Vlogsekodelete, name='Vlogsekodelete'),
    path('logsekosmemedit/<int:number>', views.Vlogsekosmemedit, name='Vlogsekosmemedit'),
    path('logsekosmemdelete/<int:number>', views.Vlogsekosmemdelete, name='Vlogsekosmemdelete'),
]
