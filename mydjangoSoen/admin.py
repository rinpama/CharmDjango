from django.contrib import admin
from .models import IdModel,PostModel,BlogModel,Iddetail

from django_summernote.admin import SummernoteModelAdmin

class BlogModelAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


# Register your models here.
admin.site.register(IdModel)
admin.site.register(PostModel)
admin.site.register(Iddetail)
admin.site.register(BlogModel,BlogModelAdmin)
# admin.site.register()
