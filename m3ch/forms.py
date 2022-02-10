from django import forms
from .models import Blog

from markdownx.widgets import MarkdownxWidget


class Blogform(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'text')
        widget = {
            'text': MarkdownxWidget(),
        }
