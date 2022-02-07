from django.db import models
from markdownx.models import MarkdownxField

# Create your models here.
class IdModel(models.Model):
    name = models.CharField(max_length=20)
    # pw = models.IntegerField(default=0000)
    date = models.DateField()

    def __str__(self):
        return " NAME : " + self.name + "<br> DATE : " + str(self.date)

class PostModel(models.Model):
    title=models.CharField(max_length=20)
    text=MarkdownxField('本文',help_text='MarkDown形式で入力してください')