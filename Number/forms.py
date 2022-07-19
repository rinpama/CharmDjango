from django import forms
from .models import *

class wagesF(forms.ModelForm):
    class Meta:
        model=wagesM
        fields='__all__'

class steelPartsF(forms.ModelForm):
    class Meta:
        model = steelPartsM
        # fields='__all__'
        fields=['firstDay','SM','WM','CC']

class upPercentF(forms.Form):
    wagesUp=forms.IntegerField(label='工賃UP率「」％',initial=100,help_text='工賃のアップ率を記入してください。0%と記入するとERROR。')
    partsUp=forms.IntegerField(label='材料価格UP率「」％',initial=100,help_text='材料のアップ率を記入してください。0%と記入するとERROR。')