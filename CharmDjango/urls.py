"""CharmDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('Soen.urls')),
    path('m3ch/', include('m3ch.urls')),
    path('show/',include('Show.urls')),
    # path('summernote/', include('django_summernote.urls')),
    # path('markdownx/', include('markdownx.urls')),
    path('actualSpot/',include('actualSpot.urls')),
    path('reimex/',include('reimex.urls')),

]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
# # 開発環境でのメディアファイルの配信設定 if settings.DEBUG:
# urlpatterns += static(
#     settings.MEDIA_URL,
#     document_root=settings.MEDIA_ROOT)
from Soen.views import my_customized_server_error
handler500 = my_customized_server_error
from m3ch.views import my_customized_server_error
handler500 = my_customized_server_error
from Show.views import my_customized_server_error
handler500 = my_customized_server_error
from actualSpot.views import my_customized_server_error
handler500 = my_customized_server_error
from reimex.views import my_customized_server_error
handler500 = my_customized_server_error