from django import forms
from .models import IdModel


class IdSearch(forms.Form):  # index
    name = forms.CharField(label='name', max_length=15)


class IdForm(forms.ModelForm):  # create
    class Meta:
        model = IdModel
        widgets = {'date': forms.SelectDateWidget}
        fields = ['name', 'date']
# class idpwForm(forms.Form):
#     name = forms.CharField(label='name', max_length=20)
#     pw = forms.DateField(label='pw')
