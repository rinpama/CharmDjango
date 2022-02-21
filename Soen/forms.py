from django import forms
from .models import MemberM,MemberDetailM,BlogM
from django_summernote.widgets import SummernoteWidget

class IdSearch(forms.Form):  # index
    name = forms.CharField(label='name', max_length=15)

class FindForm(forms.Form):
    findname = forms.CharField(label='なまえ', max_length=30, required=False)
    findadd = forms.CharField(label='アドレス',max_length=60, required=False)

class MemberF(forms.ModelForm):
    # bloodtype = forms.CharField(max_length=5)
    # age = forms.IntegerField()
    # title = forms.CharField(max_length=50)
    # text = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = MemberM
        # fields =['name','add','tel','bloodtype','age','title','text']
        fields='__all__'


class MemberDetailF(forms.ModelForm):
    class Meta:
        model=MemberDetailM
        fields=['bloodtype','age']

class BlogF(forms.ModelForm):
    class Meta:
        model=BlogM
        fields = ['title', 'text']
        widgets = {'text': SummernoteWidget(),}

