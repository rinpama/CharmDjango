from django.db import models

# Create your models here.
class wagesM(models.Model):
    ceiling300=models.IntegerField('軽鉄天井下地組')
    wall50=models.IntegerField('軽鉄壁下地W50')
    wall65=models.IntegerField('軽鉄壁下地W65')
    wall75=models.IntegerField('軽鉄壁下地W75')
    wall90=models.IntegerField('軽鉄壁下地W90')
    wall100 = models.IntegerField('軽鉄壁下地W100')

class steelPartsM(models.Model):
    firstDay=models.DateField('摘要期日~',help_text='[例］2022-12-21　⇐日付は「-」(ﾊｲﾌﾝ)で繋げてください')
    SM = models.IntegerField('ｼﾝｸﾞﾙﾊﾞｰ',help_text='5m定尺')
    WM = models.IntegerField('ﾀﾞﾌﾞﾙﾊﾞｰ', )
    CC = models.IntegerField('Cチャン', )
    def __str__(self):
        return 'steel'+str(self.firstDay)