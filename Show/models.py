from django.db import models
from Soen.models import MemberMo


class ActualSpotMo(models.Model):
    AsName = models.CharField('現場名', max_length=20, default=' 現場')
    AsCompany = models.CharField('元請会社名', max_length=60, default='株式会社', blank=True, null=True)
    AsManager = models.CharField('現場所長名', max_length=60, default=' 所長', blank=True, null=True)
    AsPostcode = models.CharField('郵便番号', max_length=60, default='857-', blank=True, null=True)
    AsAddress = models.CharField('現場住所', max_length=60, default='佐世保市', blank=True, null=True)
    Astel = models.CharField('電話番号', max_length=15, default='0956-', blank=True, null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return " 現場ID : "+ str(self.id) +" 現場名 : "+  str(self.AsName) + " (住所 : " + str(self.AsAddress) + ')'

class AsSoenMo(models.Model):
    actualspot = models.OneToOneField(ActualSpotMo, related_name='actualspot',
                                   on_delete=models.CASCADE,default='-' )  # , blank=True, null=True
    # actualspot=models.ForeignKey(ActualSpotMo,related_name='actualspot',on_delete=models.CASCADE,)#, blank=True, null=True
    AsSManager = models.ManyToManyField(MemberMo, related_name='soenmanager', blank=True,default='-')#, null=True
    AsSMember = models.ManyToManyField(MemberMo, related_name='soenmember', blank=True,default='-')#, null=True
    ConstractionDetails = models.CharField('工事内容', max_length=50, default='金属･内装工事')
    ContractDate = models.DateField('契約日', blank=True, null=True,default='2022-04-01')
    StartDate = models.DateField('工期開始日', blank=True, null=True,default='2022-04-01')
    EndDate = models.DateField('工期終了日', blank=True, null=True,default='2023-03-31')
    def __str__(self):
        return " SoenMID : "+ str(self.id) +'(('+   str(self.actualspot)+'))'

