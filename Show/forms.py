from django import forms
from Soen.models import MemberMo
from .models import ActualSpotMo,AsSoenMo

class ActualSpotF(forms.ModelForm):
    class Meta:
        model = ActualSpotMo
        # fields=['AsName','AsCompany','AsManager','AsPostcode','AsAddress','Astel']#'date'
        fields='__all__'

class AsSoenF(forms.ModelForm):
    AsSMember=forms.ModelMultipleChoiceField(queryset=MemberMo.objects,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = AsSoenMo
        # fields=['AsSManager','AsSMember','ConstractionDetails','ContractDate','StartDate','EndDate']#'actualspot',
        fields = '__all__'

class AsSearchF(forms.Form):  # index
    name = forms.CharField(label='現場名', max_length=50)