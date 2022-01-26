from django import forms
from .models import IdpwModel

class IdSearch(forms.Form):  #index
    id= forms.CharField(label= 'ID', max_length= 15)

class IdpwForm(forms.ModelForm):  #create
    class Meta:
        model= IdpwModel
        widgets= {'pw': forms.SelectDateWidget}
        fields= ['name', 'pw']
# class idpwForm(forms.Form):
#     name = forms.CharField(label='name', max_length=20)
#     pw = forms.DateField(label='pw')

