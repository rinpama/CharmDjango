from django.contrib import admin
from .models import MemberM, MemberDetailM,BlogM

from django_summernote.admin import SummernoteModelAdmin

admin.site.register(MemberM)
admin.site.register(MemberDetailM)

class BlogMAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


admin.site.register(BlogM, BlogMAdmin)
