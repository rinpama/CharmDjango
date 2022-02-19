from django.contrib import admin
from .models import IdModel, BlogModel, Iddetail

from django_summernote.admin import SummernoteModelAdmin

admin.site.register(IdModel)
admin.site.register(Iddetail)

class BlogModelAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


admin.site.register(BlogModel, BlogModelAdmin)

# Register your models here.
