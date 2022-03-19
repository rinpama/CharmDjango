from django import forms
from .models import MemberMo,MemberDetailMo,BlogMo
from django_summernote.widgets import SummernoteWidget

class IdSearch(forms.Form):  # index
    name = forms.CharField(label='name', max_length=15)

class FindForm(forms.Form):
    findname = forms.CharField(label='なまえ', max_length=30, required=False)
    findadd = forms.CharField(label='アドレス',max_length=60, required=False)

# class NewMemberF(forms.ModelForm):
#     bloodtype = forms.CharField(max_length=5)
#     age = forms.IntegerField()
#     title = forms.CharField(max_length=50)
#     text = forms.CharField(widget=SummernoteWidget())
#     class Meta:
#         model = MemberMo
#         fields =['name','add','tel','bloodtype','age','title','text']


class MemberF(forms.ModelForm):
    class Meta:
        model = MemberMo
        fields='__all__'


class MemberDetailF(forms.ModelForm):
    class Meta:
        model=MemberDetailMo
        fields=['bloodtype','age']

class BlogF(forms.ModelForm):
    class Meta:
        model=BlogMo
        fields = ['title', 'text']
        widgets = {'text': SummernoteWidget(),}

