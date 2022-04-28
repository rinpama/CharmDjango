from django.contrib import admin
from .models import Blog,ImageBlog

# from markdownx.admin import MarkdownxModelAdmin
from django_summernote.admin import SummernoteModelAdmin

class ImageBlogAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(Blog)#, MarkdownxModelAdmin
admin.site.register(ImageBlog, ImageBlogAdmin)