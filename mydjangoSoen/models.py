from django.db import models


# Create your models here.
class IdpwModel(models.Model):
    name = models.CharField(max_length=20)
    # pw = models.IntegerField(default=0000)
    pw=models.DateField()

    def __str__(self):
        return "IDNAME : " + self.name + "PW : " + str(self.pw)
