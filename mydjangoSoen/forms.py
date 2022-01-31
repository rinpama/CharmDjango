from django import forms
from .models import IdModel


class IdSearch(forms.Form):  # index
    name = forms.CharField(label='name', max_length=15)


class IdForm(forms.ModelForm):  # create
    class Meta:
        model = IdModel
        widgets = {'date': forms.SelectDateWidget}
        fields = ['name', 'date']


class FindForm(forms.Form):
    findname = forms.CharField(label='なまえ', max_length=15, required=False)
    finddate = forms.DateField(label='DATE', required=False)
