from django import forms
from .models import Blog,ImageBlog
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
# from markdownx.widgets import MarkdownxWidget


class Blogform(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        # widgets = {
        #     'text': MarkdownxWidget(attrs={'class': 'textarea'}),
        # }

class ImageBlogform(forms.ModelForm):
    class Meta:
        model = ImageBlog
        fields = '__all__'#('title','text')
        widgets = {
            'text': SummernoteWidget(),
        }
