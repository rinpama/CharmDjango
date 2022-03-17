from django.contrib import admin
from .models import ActualSpotM, AsSoenM

from django_summernote.admin import SummernoteModelAdmin

admin.site.register(ActualSpotM)
admin.site.register(AsSoenM)
