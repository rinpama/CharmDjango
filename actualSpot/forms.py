from django import forms

from .models import Aspot,mostRecent,gContractor,Vehicle
from reimex.models import SoenModel

class AspotForm(forms.ModelForm):
    # members = forms.ModelMultipleChoiceField(
    #     queryset=SoenModel.objects,
    #     widget=forms.CheckboxSelectMultiple
    # )
    class Meta():
        model=Aspot
        # fields='__all__'
        fields=('checking','spotName','gContractor','superVisor','address','contractDay','constractionDetail','firstActionDay','finishActionDay','firstSubcontractor','X','XSubcontractor','Xx','XxSubcontractor' )

class MostRecentForm(forms.ModelForm):
        class Meta():
            model= mostRecent
            # fields='__all__'
            fields=['recentName']
class gContractorForm(forms.ModelForm):
        class Meta():
            model= gContractor
            fields='__all__'
      
class VehicleForm(forms.ModelForm):
        class Meta():
            model=Vehicle
            fields='__all__'
            