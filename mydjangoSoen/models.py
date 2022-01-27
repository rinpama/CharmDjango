from django.db import models


# Create your models here.
class IdModel(models.Model):
    name = models.CharField(max_length=20)
    # pw = models.IntegerField(default=0000)
    date = models.DateField()

    def __str__(self):
        return " NAME : " + self.name + "<br> DATE : " + str(self.date)
