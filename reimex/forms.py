from django import forms

from .models import SoenModel,SpecialEducationModel,SkillTraningModel,LicenceModel


class SoenModelForm(forms.ModelForm):
    class Meta():
        model= SoenModel
        # fields='__all__'
        fields= ('checking','code','name','djgroup','djgroup2','kanaName','birthday','age','occupation','refer','dateOfEmployment','workingFirstDate','yearsOfExperience','postalCode','address','telephoneNumber','familyAdd','tel','medicalCheckUp','bloodPressure','bloodType','specialHealthCheck','SHCkind','healthInsurance','HIlast4digits','pensionInsurance','employmentinsurance','EIlast4digits','retirementCooperation','specialEducation','skillTraning','licence','dateOfAdmission','file1','file2','file3','file4','file5','file6','file7','file8','file9','file10')
        labels={
            'code':'excel用検索番号',
            'name':'なまえ'
        }
        help_text={
            'name':'名前を入力して'
        }
      
    