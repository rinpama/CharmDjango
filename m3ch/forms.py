from django import forms
from .models import Blog

# from markdownx.widgets import MarkdownxWidget


class Blogform(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        # widgets = {
        #     'text': MarkdownxWidget(attrs={'class': 'textarea'}),
        # }
