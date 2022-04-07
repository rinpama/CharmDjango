from django.contrib import admin
from .models import MemberMo, MemberDetailMo,BlogMo

# from django_summernote.admin import SummernoteModelAdmin

admin.site.register(MemberMo)
admin.site.register(MemberDetailMo)

# class BlogMoAdmin(SummernoteModelAdmin):
#     summernote_fields = '__all__'


admin.site.register(BlogMo)#, BlogMoAdmin
