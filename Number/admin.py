from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
# from django_summernote.admin import SummernoteModelAdmin

admin.site.register(wagesM)
admin.site.register(steelPartsM)
