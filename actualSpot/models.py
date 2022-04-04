from django.db import models
from django.urls import reverse
# Create your models here.

from django.db.models.deletion import CASCADE
# Create your models here.
class Vehicle(models.Model):
    mrecent= models.CharField(verbose_name="所属",max_length=20,null=True,blank=True)
    vehicleNumber= models.CharField(verbose_name="車両番号",max_length=20,null=True,blank=True)
    firstUse= models.DateField(verbose_name="使用期間開始",null=True,blank=True)
    finishUse= models.DateField(verbose_name="使用期間終了",null=True,blank=True)
    vehicleModel= models.CharField(verbose_name="車検証_型式",max_length=20,null=True,blank=True)
    firstInspection= models.DateField(verbose_name="車検証_車検期間開始",null=True,blank=True)
    finishInspection= models.DateField(verbose_name="車検証_車検期間終了",null=True,blank=True)
    file1= models.FileField(verbose_name="Link1車検証",max_length=100,null=True,blank=True)
    liabilityComp= models.CharField(verbose_name="自賠責_保険会社",max_length=20,null=True,blank=True)
    liability_num= models.CharField(verbose_name="自賠責_証券番号",max_length=20,null=True,blank=True)
    firstliability= models.DateField(verbose_name="自賠責_保険期間開始",null=True,blank=True)
    finishliability= models.DateField(verbose_name="自賠責_保険期間終了",null=True,blank=True)
    file2= models.FileField(verbose_name="Link2自賠責",max_length=100,null=True,blank=True)
    voluntaryInsureComp= models.CharField(verbose_name="任意保険_保険会社",max_length=20,null=True,blank=True)
    voluntaryInsureNum= models.CharField(verbose_name="任意保険_証券番号",max_length=20,null=True,blank=True)
    firstVoluntary= models.DateField(verbose_name="任意保険_保険期間開始",null=True,blank=True)
    finishVoluntary= models.DateField(verbose_name="任意保険_保険期間終了",null=True,blank=True)
    voluntary_object= models.CharField(verbose_name="任意保険_対物_千円",max_length=20,null=True,blank=True)
    voluntary_human= models.CharField(verbose_name="任意保険_対人_千円",max_length=20,null=True,blank=True)
    voluntary_passenger= models.CharField(verbose_name="任意保険_搭乗者_千円",max_length=20,null=True,blank=True)
    file3= models.FileField(verbose_name="Link3任意保険",max_length=100,null=True,blank=True)
    driver= models.ManyToManyField('reimex.SoenModel')
    drive_departure= models.CharField(verbose_name="運転_出発地",max_length=100,null=True,blank=True)
    drive_waypoint1= models.CharField(verbose_name="運転_経由１",max_length=100,null=True,blank=True)
    drive_waypoint2= models.CharField(verbose_name="運転_経由2",max_length=100,null=True,blank=True)
    drive_arrival= models.CharField(verbose_name="運転_到着地",max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.vehicleNumber
    class Meta:
        verbose_name_plural= "車両"
    
#ｾﾞﾈｺﾝ・直近上位会社＿基本
class gContractor(models.Model):
    # Xx= models.IntegerField(verbose_name="X次",null=True,blank=True)
    gName=models.CharField(verbose_name="ｾﾞﾈｺﾝ会社名",max_length=20,null=True,blank=True)
    postalCode= models.CharField(verbose_name="郵便番号",max_length=20,null=True,blank=True)
    address= models.CharField(verbose_name="現住所",max_length=100,null=True,blank=True)
    telephoneNumber= models.CharField(verbose_name="電話番号",max_length=20,null=True,blank=True)
    FaxNumber= models.CharField(verbose_name="Fax番号",max_length=20,null=True,blank=True)
    def __str__(self):
        return self.gName
    class Meta:
        verbose_name_plural= "ｾﾞﾈｺﾝ会社"   


class mostRecent(models.Model):
    healthInsurance_list = [
        ('1','健康保険組合'),
        ('2','協会けんぽ（全国健康保険協会）'),
        ('3','各種共済組合'),
        ('4','国民健康保険'),
        ('5','国民健康保険組合（長けん国保）'),
        ('6','後期高齢者医療制度'),
        ('7','船員保険（全国健康保険協会）'),
        ('8','-')
    ]
   
    pensionInsurance_list = [
        ('1','国民年金'),
        ('2','厚生年金'),
        ('3','-'),
    ]
    employmentinsurance_list = [
        ('1','無'),
        ('2','有'),
        ('3','適用除外'),
        ('4','-'),
    ]
    free_list = [
        ('1','無'),
        ('2','有'),
        ('3','-'),
    ]
    chiji_list = [
        ('1','大臣'),
        ('2','知事'),
        ('3','-'),
    ]
    ippan_list = [
        ('1','特定'),
        ('2','一般'),
        ('3','-'),
    ]
    permit_list= [
        ('1','建築工事業'),
        ('2','内装仕上工事業'),
        ('3','-'),
    ]
    carryonMachine_list=[
        ('1','電動ｸﾞﾗｲﾝﾀﾞｰ'),
        ('2','電動ﾄﾞﾘﾙ'),
        ('3','ｺﾝﾌﾟﾚｯｻｰ'),
        ('4','アーク溶接機'),
        ('5','-'),    
    ]
    # Xx= models.IntegerField(verbose_name="X次",null=True,blank=True)
    recentName=models.CharField(verbose_name="協力会社名",max_length=20,default="companyName")
    postalCode= models.CharField(verbose_name="郵便番号",max_length=20,null=True,blank=True)
    address= models.CharField(verbose_name="現住所",max_length=100,null=True,blank=True)
    telephoneNumber= models.CharField(verbose_name="電話番号",max_length=20,null=True,blank=True)
    FaxNumber= models.CharField(verbose_name="Fax番号",max_length=20,null=True,blank=True)
    representative= models.CharField(verbose_name="代表者名",max_length=100,null=True,blank=True)
    saftyManager= models.CharField(verbose_name="安全衛生責任者",max_length=100,null=True,blank=True)
    saftyPromoter= models.CharField(verbose_name="安全衛生推進者",max_length=100,null=True,blank=True)
    leadEngineer= models.CharField(verbose_name="主任技術者",max_length=100,null=True,blank=True)
    file0= models.FileField(verbose_name="Link0",max_length=100,null=True,blank=True)
    Insurance_station= models.CharField(verbose_name="保険＿事業所名",max_length=100,null=True,blank=True)
    Insurance_station_number= models.CharField(verbose_name="保険＿事業所名_整理記号･番号",max_length=100,null=True,blank=True)
    healthInsurance= models.CharField(verbose_name="健康保険",max_length=100,null=True,blank=True,choices=healthInsurance_list)
    file1= models.FileField(verbose_name="Link1",max_length=100,null=True,blank=True)
    pensionInsurance= models.CharField(verbose_name="年金保険",max_length=100,null=True,blank=True,choices=pensionInsurance_list)
    file2= models.FileField(verbose_name="Link2",max_length=100,null=True,blank=True)
    employmentinsurance= models.CharField(verbose_name="雇用保険",max_length=100,null=True,blank=True,choices=employmentinsurance_list)
    employmentinsurance_number= models.CharField(verbose_name="雇用保険番号",max_length=100,null=True,blank=True)
    file3= models.FileField(verbose_name="Link3",max_length=100,null=True,blank=True)
    retirementCooperation= models.CharField(verbose_name="建退協",max_length=100,null=True,blank=True,choices=free_list)
    file4= models.FileField(verbose_name="Link4",max_length=100,null=True,blank=True)
    constractionPermit= models.CharField(verbose_name="建設業許可業種",max_length=100,null=True,blank=True,choices=permit_list)
    constractionPermit_chuji= models.CharField(verbose_name="建設業許可_大臣・知事",max_length=100,null=True,blank=True,choices=chiji_list)
    constractionPermit_ippan= models.CharField(verbose_name="建設業許可_特定・一般",max_length=100,null=True,blank=True,choices=ippan_list)
    constractionPermit_nendo= models.CharField(verbose_name="建設業許可_年度",max_length=100,null=True,blank=True)
    constractionPermit_num= models.CharField(verbose_name="建設業許可_番号",max_length=100,null=True,blank=True)
    constractionPermit_gat= models.DateField(verbose_name="建設業許可_取得年月日",null=True,blank=True)
    file5= models.FileField(verbose_name="Link5",max_length=100,null=True,blank=True)
    contractDay= models.DateField(verbose_name="工事契約日",null=True,blank=True)
    firstActionDay= models.DateField(verbose_name="請負開始工期",null=True,blank=True)
    finishActionDay= models.DateField(verbose_name="請負終了工期",null=True,blank=True)
    contractionDetail= models.CharField(verbose_name="工事内容",max_length=100,null=True,blank=True)
    No_1_specific_skill_foreigner= models.CharField(verbose_name="一号特定技能外国人",max_length=100,null=True,blank=True,choices=free_list)
    foreignWorker= models.CharField(verbose_name="外国人建設就労者",max_length=100,null=True,blank=True,choices=free_list)
    foreignIntern= models.CharField(verbose_name="外国人技能実習生",max_length=100,null=True,blank=True,choices=free_list)
    carryonMachine= models.CharField(verbose_name="持込機械",max_length=100,null=True,blank=True,choices=carryonMachine_list)
    vehicle= models.ManyToManyField('Vehicle')  #車両vehicle
    mobileCrane= models.CharField(verbose_name="移動式ｸﾚｰﾝ･車両系建設機械",max_length=100,null=True,blank=True)
    dangerous= models.CharField(verbose_name="危険物OR有機溶剤OR特定化学物質",max_length=100,null=True,blank=True)
    
    members=models.ManyToManyField('reimex.SoenModel')
    
    def __str__(self):
        return self.recentName
    class Meta:
        verbose_name_plural= "協力会社"
        
#作業現場情報
class Aspot(models.Model):
    checking=models.BooleanField(verbose_name="選択フラグ",default=False)
    spotName= models.CharField(verbose_name="現場名",max_length=50,default='必須')
    gContractor=models.ManyToManyField('gContractor',null=True,blank=True) #ｾﾞﾈ会社
    superVisor= models.CharField(verbose_name="現場所長名",max_length=50,default='必須')
    address=models.CharField(max_length=50,verbose_name="現場住所",null=True,blank=True)
    contractDay= models.DateField(verbose_name="ｾﾞﾈ請負契約日",null=True,blank=True)
    constractionDetail= models.CharField(verbose_name="ｾﾞﾈ工事内容",max_length=50,null=True,blank=True)
    firstActionDay= models.DateField(verbose_name="全体開始工期",null=True,blank=True)
    finishActionDay= models.DateField(verbose_name="全体終了工期",null=True,blank=True)
    firstSubcontractor=models.CharField(verbose_name="上位会社",max_length=50,null=True,blank=True)
    X= models.IntegerField(verbose_name="X次",default='1')
    XSubcontractor= models.ManyToManyField('mostRecent',null=True,blank=True) #基本装苑
    Xx= models.IntegerField(verbose_name="Xx次",default='2')
    XxSubcontractor= models.ManyToManyField('reimex.SoenModel',null=True,blank=True) #協力会社
    
    
    
    
    def __str__(self):
        return self.spotName
    def get_absolute_url(self):
        return reverse("actualSpot.spotlist")
    class Meta:
        verbose_name_plural= "現場名"   