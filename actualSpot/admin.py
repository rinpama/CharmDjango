from django.contrib import admin

# Register your models here.
from .models import mostRecent,Aspot,gContractor,Vehicle
admin.site.register(mostRecent)
admin.site.register(Aspot)
admin.site.register(gContractor)
admin.site.register(Vehicle)