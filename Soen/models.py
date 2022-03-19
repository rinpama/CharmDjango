from django.db import models
from markdownx.models import MarkdownxField


# Create your models here.
class MemberMo(models.Model):
    name = models.CharField('名前', max_length=20, default='new_name')
    add = models.CharField('住所', max_length=60, default='sasebo', blank=True, null=True)
    tel = models.CharField('電話番号', max_length=15, default='0956-', blank=True, null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str( self.id)+ " 名前 : " + self.name + " (住所 : " + str(self.add) + ')'


class MemberDetailMo(models.Model):
    memberm = models.ForeignKey(MemberMo, related_name='detail', on_delete=models.CASCADE)
    bloodtype = models.CharField('血液型', max_length=10, blank=True, null=True,default='A')
    age = models.IntegerField('年齢', blank=True, null=True,default='0')
    def __str__(self):
        return str(self.age)

# summernoteModel
class BlogMo(models.Model):
    memberm2 = models.ForeignKey(MemberMo, on_delete=models.CASCADE, related_name='blog')
    title = models.CharField('ﾀｲﾄﾙ', max_length=50, blank=True, null=True,default='title')
    text = models.TextField('ﾃｷｽﾄ & ﾌｫﾄ', blank=True, null=True,default='text')
    created_at = models.DateField('作成日', auto_now_add=True)
    updated_at = models.DateField('更新日', auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'ブログ'
        verbose_name_plural = 'sプログ'


from django.db import models

# Create your models here.
