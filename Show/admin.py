from django.contrib import admin
from .models import ActualSpotMo, AsSoenMo

from django_summernote.admin import SummernoteModelAdmin

admin.site.register(ActualSpotMo)
admin.site.register(AsSoenMo)
