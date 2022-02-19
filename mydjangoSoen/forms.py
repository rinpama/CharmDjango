from django import forms
from .models import IdModel,Iddetail,BlogModel
from django_summernote.widgets import SummernoteWidget

class IdSearch(forms.Form):  # index
    name = forms.CharField(label='name', max_length=15)

class FindForm(forms.Form):
    findname = forms.CharField(label='なまえ', max_length=30, required=False)
    findadd = forms.CharField(label='アドレス',max_length=60, required=False)

class IdForm(forms.ModelForm):
    bloodtype = forms.CharField(max_length=5)
    age = forms.IntegerField()
    title = forms.CharField(max_length=50)
    text = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = IdModel
        fields =['name','add','tel','bloodtype','age','title','text']


class IddetailForm(forms.ModelForm):
    pass
    # class Meta:
    #     model=Iddetail
    #     fields=['bloodtype','age']

class BlogForm(forms.ModelForm):
    pass
    # class Meta:
    #     model=BlogModel
    #     fields = ['title', 'text']
    #     widgets = {
    #         'text': SummernoteWidget(),
    #     }

