from django.contrib import admin

# Register your models here.
from .models import SoenModel
admin.site.register(SoenModel)


from .models import SpecialEducationModel,SkillTraningModel,LicenceModel
admin.site.register(SpecialEducationModel)
admin.site.register(SkillTraningModel)
admin.site.register(LicenceModel)

