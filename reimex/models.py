from django.db import models
from django.urls import reverse
# Create your models here.

from django.db.models.deletion import CASCADE

# Create your models here.
#soenmodel特別教育_選択
class SpecialEducationModel(models.Model):
    specialeducation_list=[
        ('-','-'),
        ('研削といし取替・試運転','研削といし取替・試運転'),
        ('アーク溶接作業','アーク溶接作業'),
        ('フォークリフト運転業務','フォークリフト運転業務'),
        ('高所作業車の運転','高所作業車の運転'),
        ('巻き上げ機の運転','巻き上げ機の運転'),
        ('クレーンの運転','クレーンの運転'),
        ('移動式クレーンの運転','移動式クレーンの運転'),
        ('玉掛け業務','玉掛け業務'),
        ('職長教育','職長教育'),
        ('職長教育（追教育）','職長教育（追教育）'),
        ('安全衛生責任者','安全衛生責任者'),
        ('足場組立等作業従事者特別教育','足場組立等作業従事者特別教育'),
        ('有機溶剤取扱い業務','有機溶剤取扱い業務'),
        ('特別教育14','特別教育14'),
        ('特別教育15','特別教育15'),
        ('特別教育16','特別教育16'),
        ('特別教育17','特別教育17'),
        ('特別教育18','特別教育18'),
        ('特別教育19','特別教育19'),
        ('特別教育20','特別教育20'),
    ]
    name=models.CharField(verbose_name="特別教育",max_length=30,null=True,blank=True,choices=specialeducation_list)
    def __str__(self):
        return self.name
#soenmodel技能講習_選択
class SkillTraningModel(models.Model):
    skillTraning_list=[
        ('-','-'),
        ('有機溶剤作業主任者','有機溶剤作業主任者'),
        ('玉掛け技能講習','玉掛け技能講習'),
        ('特定化学物質等作業主任者','特定化学物質等作業主任者'),
        ('小型移動式クレン運転技能講習','小型移動式クレン運転技能講習'),
        ('高所作業車運転技能講習','高所作業車運転技能講習'),
        ('技能講習6','技能講習6'),
        ('技能講習7','技能講習7'),
        ('技能講習8','技能講習8'),
        ('技能講習9','技能講習9'),
        ('技能講習10','技能講習10'),
        ('技能講習11','技能講習11'),
        ('技能講習12','技能講習12'),
        ('技能講習13','技能講習13'),
        ('技能講習14','技能講習14'),
        ('技能講習15','技能講習15'),
        ('技能講習16','技能講習16'),
        ('技能講習17','技能講習17'),
        ('技能講習18','技能講習18'),
        ('技能講習19','技能講習19'),
        ('技能講習20','技能講習20'),
    ]
    name=models.CharField(verbose_name="技能講習",max_length=30,null=True,blank=True,choices=skillTraning_list)
    def __str__(self):
        return self.name    
#soenmodel免許_選択
class LicenceModel(models.Model):
    
    licence_list=[
        ('-','-'),
        ('1級建築士','1級建築士'),
        ('2級建築士','2級建築士'),
        ('1級建築施工管理技士','1級建築施工管理技士'),
        ('2級建築施工管理技士（建築）','2級建築施工管理技士（建築）'),
        ('2級建築施工管理技士（仕上げ）','2級建築施工管理技士（仕上げ）'),
        ('1級技能士　内装仕上げ施工（鋼製下地工事作業）','1級技能士　内装仕上げ施工（鋼製下地工事作業）'),
        ('2級技能士　内装仕上げ施工（鋼製下地工事作業）','2級技能士　内装仕上げ施工（鋼製下地工事作業）'),
        ('1級技能士　内装仕上げ施工（ﾎﾞｰﾄﾞ仕上げ工事作業）','1級技能士　内装仕上げ施工（ﾎﾞｰﾄﾞ仕上げ工事作業）'),
        ('2級技能士　内装仕上げ施工（ﾎﾞｰﾄﾞ仕上げ工事作業）','2級技能士　内装仕上げ施工（ﾎﾞｰﾄﾞ仕上げ工事作業）'),
        ('1級技能士　内装仕上げ施工（ﾌﾟﾗｽﾁｯｸ系床仕上げ工事作業）','1級技能士　内装仕上げ施工（ﾌﾟﾗｽﾁｯｸ系床仕上げ工事作業）'),
        ('2級技能士　内装仕上げ施工（ﾌﾟﾗｽﾁｯｸ系床仕上げ工事作業）','2級技能士　内装仕上げ施工（ﾌﾟﾗｽﾁｯｸ系床仕上げ工事作業）'),
        ('1級技能士　内装仕上げ施工（ｶｰﾍﾟｯﾄ系床仕上げ工事作業）','1級技能士　内装仕上げ施工（ｶｰﾍﾟｯﾄ系床仕上げ工事作業）'),
        ('2級技能士　内装仕上げ施工（ｶｰﾍﾟｯﾄ系床仕上げ工事作業）','2級技能士　内装仕上げ施工（ｶｰﾍﾟｯﾄ系床仕上げ工事作業）'),
        ('1級技能士　表装（表具作業）','1級技能士　表装（表具作業）'),
        ('2級技能士　表装（表具作業）','2級技能士　表装（表具作業）'),
        ('1級技能士','1級技能士'),
        ('2級技能士','2級技能士'),
        ('3級技能士','3級技能士'),
        ('自動車運転免許','自動車運転免許'),
        ('免許20','免許20'),
        ]
    name=models.CharField(verbose_name="免許",max_length=40,null=True,blank=True,choices=licence_list)
    def __str__(self):
        return self.name

#装苑メンバー（作業員名簿、施工体制台帳？）
class SoenModel(models.Model):
    healthInsurance_list = [
        ('1','健康保険組合'),
        ('2','協会けんぽ（全国健康保険協会）'),
        ('3','各種共済組合'),
        ('4','国民健康保険'),
        ('5','国民健康保険組合（長けん国保）'),
        ('6','後期高齢者医療制度'),
        ('7','船員保険（全国健康保険協会）'),
        ('8','-'),
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
    retirementCooperation_list=[
        ('1','有'),
        ('2','無'),
        ('3','-'),
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
    checking=models.BooleanField(verbose_name="選択フラグ（ゴメン今のところ使いません⇒）",default=False)
    code=models.IntegerField(verbose_name="検索番号")
    djgroup= models.CharField(verbose_name="会社名(親方内装)",max_length=100,default=' 内装')
    name= models.CharField(verbose_name="代表者姓名",max_length=20,null=True,blank=True)
    kanaName= models.CharField(verbose_name="ﾅﾏｴ",max_length=20,null=True,blank=True)
    djgroup2= models.CharField(verbose_name="所属(souen)",max_length=100,null=True,blank=True,default='装苑 or')
    occupation= models.CharField(verbose_name="職種",max_length=100,null=True,blank=True)
    refer= models.CharField(verbose_name="※1",max_length=100,default='内装工事')
    birthday= models.DateField(verbose_name="生年月日",null=True,blank=True)
    age= models.CharField(verbose_name="年齢",max_length=20,null=True,blank=True)
    dateOfEmployment= models.DateField(verbose_name="雇用年月日",null=True,blank=True)
    workingFirstDate= models.CharField(verbose_name="該当職種に就労した年齢",max_length=20,null=True,blank=True)
    yearsOfExperience= models.CharField(verbose_name="経験年数",max_length=20,null=True,blank=True)
    postalCode= models.CharField(verbose_name="郵便番号",max_length=20,null=True,blank=True)
    address= models.CharField(verbose_name="現住所",max_length=100,null=True,blank=True)
    telephoneNumber= models.CharField(verbose_name="電話番号",max_length=20,null=True,blank=True)
    familyAdd= models.CharField(verbose_name="家族連絡先",max_length=100,default='同上')
    tel= models.CharField(verbose_name="電話番号",max_length=20,null=True,blank=True)
    medicalCheckUp= models.DateField(verbose_name="健康診断日",null=True,blank=True)
    bloodPressure= models.CharField(verbose_name="血圧",max_length=20,null=True,blank=True)
    bloodType= models.CharField(verbose_name="血液型",max_length=20,null=True,blank=True)
    specialHealthCheck= models.CharField(verbose_name="特殊健康診断",max_length=100,null=True,blank=True)
    SHCkind= models.CharField(verbose_name="種類",max_length=100,null=True,blank=True)
    saftyManager= models.CharField(verbose_name="安全衛生責任者",max_length=100,null=True,blank=True)
    saftyPromoter= models.CharField(verbose_name="安全衛生推進者",max_length=100,null=True,blank=True)
    leadEngineer= models.CharField(verbose_name="主任技術者",max_length=100,null=True,blank=True)
    file0= models.FileField(verbose_name="Link0",max_length=100,null=True,blank=True)
    Insurance_station= models.CharField(verbose_name="保険＿事業所名",max_length=100,null=True,blank=True)
    Insurance_station_number= models.CharField(verbose_name="保険＿事業所名_整理記号･番号",max_length=100,null=True,blank=True)
    healthInsurance= models.CharField(verbose_name="健康保険",max_length=100,null=True,blank=True,choices = healthInsurance_list)
    HIlast4digits= models.CharField(verbose_name="健康保険下4桁",max_length=100,null=True,blank=True)
    file1= models.FileField(verbose_name="Link1健康保険",max_length=100,null=True,blank=True,default="\\Soensv\共有フォルダ\新しいフォルダー")
    pensionInsurance= models.CharField(verbose_name="年金保険",max_length=100,null=True,blank=True,choices = pensionInsurance_list)
    file2= models.FileField(verbose_name="Link2年金保険",max_length=100,null=True,blank=True)
    employmentinsurance= models.CharField(verbose_name="雇用保険",max_length=100,null=True,blank=True,choices = employmentinsurance_list)
    EIlast4digits= models.CharField(verbose_name="雇用保険下4桁",max_length=100,null=True,blank=True)
    file3= models.FileField(verbose_name="Link3雇用保険",max_length=100,null=True,blank=True)
    retirementCooperation= models.CharField(verbose_name="建退協",max_length=100,null=True,blank=True,choices=retirementCooperation_list)
    file4= models.FileField(verbose_name="Link4建退協",max_length=100,null=True,blank=True)
    specialEducation= models.ManyToManyField(SpecialEducationModel,null=True,blank=True)
    file5= models.FileField(verbose_name="Link5雇用・職長・特別教育",max_length=100,null=True,blank=True)
    skillTraning= models.ManyToManyField(SkillTraningModel,null=True,blank=True)
    file6= models.FileField(verbose_name="Link6技能講習",max_length=100,null=True,blank=True)
    licence=models.ManyToManyField(LicenceModel,null=True,blank=True)
    file7= models.FileField(verbose_name="Link免許",max_length=100,null=True,blank=True)
    driverLicence_number= models.CharField(verbose_name="自動車免許番号",max_length=100,null=True,blank=True)
    file8= models.FileField(verbose_name="Link自動車免許証",max_length=100,null=True,blank=True)
    dateOfAdmission= models.DateField(verbose_name="入場年月日",null=True,blank=True)
    file9= models.FileField(verbose_name="Link9",max_length=100,null=True,blank=True)
    file10= models.FileField(verbose_name="Link10",max_length=100,null=True,blank=True)
    
    # rewrite=models.DateField(auto_now_add=True,null=True,blank=True) 
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
    mvehicle= models.ManyToManyField('actualSpot.Vehicle',null=True,blank=True)  #車両vehicle
    mobileCrane= models.CharField(verbose_name="移動式ｸﾚｰﾝ･車両系建設機械",max_length=100,null=True,blank=True)
    dangerous= models.CharField(verbose_name="危険物OR有機溶剤OR特定化学物質",max_length=100,null=True,blank=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("reimex:screate", kwargs={"pk": self.pk})
    class Meta:
        verbose_name_plural= "そうえんメンバー"   

