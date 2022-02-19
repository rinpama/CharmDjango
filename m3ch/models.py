from django.db import models
from markdownx.models import MarkdownxField

from django.utils.safestring import mark_safe
from markdownx.utils import markdownify

# Create your models here.

#Markdownx
class Blog(models.Model):
    title= models.CharField('ﾀｲﾄﾙ',max_length=50)
    text= MarkdownxField('ﾃｷｽﾄ',help_text='ﾏｰｸﾀﾞｳﾝ形式で書いてください')
    create_at=models.DateField('作成日',auto_now_add=True)
    update_at=models.DateField('更新日',auto_now=True)
    def get_text_mark_down(self):
        return mark_safe(markdownify(self.text))
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='ブログ'
        verbose_name_plural='ブログ'

# summernoteModel
class ImageBlog(models.Model):
    title = models.CharField('ﾀｲﾄﾙ', max_length=50)
    text = models.TextField('ﾃｷｽﾄ', blank=True, null=True)
    created_at = models.DateField('作成日', auto_now_add=True)
    updated_at = models.DateField('更新日', auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'mIMブログ'
        verbose_name_plural = 'mimプログ'