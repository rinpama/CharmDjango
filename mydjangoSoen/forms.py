from django import forms
from .models import IdModel


class IdSearch(forms.Form):  # index
    name = forms.CharField(label='name', max_length=15)


class IdForm(forms.ModelForm):  # create
    class Meta:
        model = IdModel
        # widgets = {'date': forms.SelectDateWidget}
        fields ='__all__'
        # ['name', 'date']

class FindForm(forms.Form):
    findname = forms.CharField(label='なまえ', max_length=30, required=False)
    findadd = forms.CharField(label='アドレス',max_length=60, required=False)
