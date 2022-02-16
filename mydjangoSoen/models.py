from django.db import models
from markdownx.models import MarkdownxField


# Create your models here.
class IdModel(models.Model):
    name = models.CharField('名前',max_length=20, default='new_name')
    add = models.CharField('住所',max_length=60, default='sasebo')
    tel = models.CharField('電話番号',max_length=15, default='0956-')
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return " 名前 : " + self.name + " (住所 : " + str(self.add) + ')'


class Iddetail(models.Model):
    bloodtype = models.CharField('血液型',max_length=10)
    age = models.IntegerField('年齢',)
    IdModel = models.ForeignKey(IdModel, related_name='mroedetail', on_delete=models.CASCADE)
    def __str__(self):
        return self.IdModel


# Markdownx
class PostModel(models.Model):
    title = models.CharField(max_length=20)
    text = MarkdownxField('本文', help_text='MarkDown形式で入力してください')


# summernoteModel
class BlogModel(models.Model):
    title = models.CharField('ﾀｲﾄﾙ', max_length=50)
    text = models.TextField('ﾃｷｽﾄ', blank=True, null=True)
    created_at = models.DateField('作成日', auto_now_add=True)
    updated_at = models.DateField('更新日', auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'ブログ'
        verbose_name_plural = 'プログ'

