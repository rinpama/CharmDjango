from django import forms
from Soen.models import MemberM
from .models import ActualSpotM,AsSoenM

class ActualSpotF(forms.ModelForm):
    class Meta:
        model = ActualSpotM
        fields='__all__'

class AsSoenF(forms.ModelForm):
    AsSMember=forms.ModelMultipleChoiceField(queryset=MemberM.objects,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = AsSoenM
        fields=['AsSManager','AsSManager','AsSMember','ConstractionDetails','ContractDate','StartDate','EndDate']

class AsSearchF(forms.Form):  # index
    name = forms.CharField(label='現場名', max_length=50)