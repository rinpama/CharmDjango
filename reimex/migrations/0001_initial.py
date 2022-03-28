# Generated by Django 4.0.1 on 2022-03-28 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actualSpot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LicenceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('-', '-'), ('1級建築士', '1級建築士'), ('2級建築士', '2級建築士'), ('1級建築施工管理技士', '1級建築施工管理技士'), ('2級建築施工管理技士（建築）', '2級建築施工管理技士（建築）'), ('2級建築施工管理技士（仕上げ）', '2級建築施工管理技士（仕上げ）'), ('1級技能士\u3000内装仕上げ施工（鋼製下地工事作業）', '1級技能士\u3000内装仕上げ施工（鋼製下地工事作業）'), ('2級技能士\u3000内装仕上げ施工（鋼製下地工事作業）', '2級技能士\u3000内装仕上げ施工（鋼製下地工事作業）'), ('1級技能士\u3000内装仕上げ施工（ﾎﾞｰﾄﾞ仕上げ工事作業）', '1級技能士\u3000内装仕上げ施工（ﾎﾞｰﾄﾞ仕上げ工事作業）'), ('2級技能士\u3000内装仕上げ施工（ﾎﾞｰﾄﾞ仕上げ工事作業）', '2級技能士\u3000内装仕上げ施工（ﾎﾞｰﾄﾞ仕上げ工事作業）'), ('1級技能士\u3000内装仕上げ施工（ﾌﾟﾗｽﾁｯｸ系床仕上げ工事作業）', '1級技能士\u3000内装仕上げ施工（ﾌﾟﾗｽﾁｯｸ系床仕上げ工事作業）'), ('2級技能士\u3000内装仕上げ施工（ﾌﾟﾗｽﾁｯｸ系床仕上げ工事作業）', '2級技能士\u3000内装仕上げ施工（ﾌﾟﾗｽﾁｯｸ系床仕上げ工事作業）'), ('1級技能士\u3000内装仕上げ施工（ｶｰﾍﾟｯﾄ系床仕上げ工事作業）', '1級技能士\u3000内装仕上げ施工（ｶｰﾍﾟｯﾄ系床仕上げ工事作業）'), ('2級技能士\u3000内装仕上げ施工（ｶｰﾍﾟｯﾄ系床仕上げ工事作業）', '2級技能士\u3000内装仕上げ施工（ｶｰﾍﾟｯﾄ系床仕上げ工事作業）'), ('1級技能士\u3000表装（表具作業）', '1級技能士\u3000表装（表具作業）'), ('2級技能士\u3000表装（表具作業）', '2級技能士\u3000表装（表具作業）'), ('1級技能士', '1級技能士'), ('2級技能士', '2級技能士'), ('3級技能士', '3級技能士'), ('自動車運転免許', '自動車運転免許'), ('免許20', '免許20')], max_length=40, null=True, verbose_name='免許')),
            ],
        ),
        migrations.CreateModel(
            name='SkillTraningModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('-', '-'), ('有機溶剤作業主任者', '有機溶剤作業主任者'), ('玉掛け技能講習', '玉掛け技能講習'), ('特定化学物質等作業主任者', '特定化学物質等作業主任者'), ('小型移動式クレン運転技能講習', '小型移動式クレン運転技能講習'), ('高所作業車運転技能講習', '高所作業車運転技能講習'), ('技能講習6', '技能講習6'), ('技能講習7', '技能講習7'), ('技能講習8', '技能講習8'), ('技能講習9', '技能講習9'), ('技能講習10', '技能講習10'), ('技能講習11', '技能講習11'), ('技能講習12', '技能講習12'), ('技能講習13', '技能講習13'), ('技能講習14', '技能講習14'), ('技能講習15', '技能講習15'), ('技能講習16', '技能講習16'), ('技能講習17', '技能講習17'), ('技能講習18', '技能講習18'), ('技能講習19', '技能講習19'), ('技能講習20', '技能講習20')], max_length=30, null=True, verbose_name='技能講習')),
            ],
        ),
        migrations.CreateModel(
            name='SpecialEducationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('-', '-'), ('研削といし取替・試運転', '研削といし取替・試運転'), ('アーク溶接作業', 'アーク溶接作業'), ('フォークリフト運転業務', 'フォークリフト運転業務'), ('高所作業車の運転', '高所作業車の運転'), ('巻き上げ機の運転', '巻き上げ機の運転'), ('クレーンの運転', 'クレーンの運転'), ('移動式クレーンの運転', '移動式クレーンの運転'), ('玉掛け業務', '玉掛け業務'), ('職長教育', '職長教育'), ('職長教育（追教育）', '職長教育（追教育）'), ('安全衛生責任者', '安全衛生責任者'), ('足場組立等作業従事者特別教育', '足場組立等作業従事者特別教育'), ('有機溶剤取扱い業務', '有機溶剤取扱い業務'), ('特別教育14', '特別教育14'), ('特別教育15', '特別教育15'), ('特別教育16', '特別教育16'), ('特別教育17', '特別教育17'), ('特別教育18', '特別教育18'), ('特別教育19', '特別教育19'), ('特別教育20', '特別教育20')], max_length=30, null=True, verbose_name='特別教育')),
            ],
        ),
        migrations.CreateModel(
            name='SoenModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checking', models.BooleanField(default=False, verbose_name='選択フラグ（ゴメン今のところ使いません⇒）')),
                ('code', models.IntegerField(verbose_name='検索番号')),
                ('djgroup', models.CharField(default=' 内装', max_length=100, verbose_name='会社名(親方内装)')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='代表者姓名')),
                ('kanaName', models.CharField(blank=True, max_length=20, null=True, verbose_name='ﾅﾏｴ')),
                ('djgroup2', models.CharField(blank=True, default='装苑 or', max_length=100, null=True, verbose_name='所属(souen)')),
                ('occupation', models.CharField(blank=True, max_length=100, null=True, verbose_name='職種')),
                ('refer', models.CharField(default='内装工事', max_length=100, verbose_name='※1')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='生年月日')),
                ('age', models.CharField(blank=True, max_length=20, null=True, verbose_name='年齢')),
                ('dateOfEmployment', models.DateField(blank=True, null=True, verbose_name='雇用年月日')),
                ('workingFirstDate', models.CharField(blank=True, max_length=20, null=True, verbose_name='該当職種に就労した年齢')),
                ('yearsOfExperience', models.CharField(blank=True, max_length=20, null=True, verbose_name='経験年数')),
                ('postalCode', models.CharField(blank=True, max_length=20, null=True, verbose_name='郵便番号')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='現住所')),
                ('telephoneNumber', models.CharField(blank=True, max_length=20, null=True, verbose_name='電話番号')),
                ('familyAdd', models.CharField(default='同上', max_length=100, verbose_name='家族連絡先')),
                ('tel', models.CharField(blank=True, max_length=20, null=True, verbose_name='電話番号')),
                ('medicalCheckUp', models.DateField(blank=True, null=True, verbose_name='健康診断日')),
                ('bloodPressure', models.CharField(blank=True, max_length=20, null=True, verbose_name='血圧')),
                ('bloodType', models.CharField(blank=True, max_length=20, null=True, verbose_name='血液型')),
                ('specialHealthCheck', models.CharField(blank=True, max_length=100, null=True, verbose_name='特殊健康診断')),
                ('SHCkind', models.CharField(blank=True, max_length=100, null=True, verbose_name='種類')),
                ('saftyManager', models.CharField(blank=True, max_length=100, null=True, verbose_name='安全衛生責任者')),
                ('saftyPromoter', models.CharField(blank=True, max_length=100, null=True, verbose_name='安全衛生推進者')),
                ('leadEngineer', models.CharField(blank=True, max_length=100, null=True, verbose_name='主任技術者')),
                ('file0', models.FileField(blank=True, null=True, upload_to='', verbose_name='Link0')),
                ('Insurance_station', models.CharField(blank=True, max_length=100, null=True, verbose_name='保険＿事業所名')),
                ('Insurance_station_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='保険＿事業所名_整理記号･番号')),
                ('healthInsurance', models.CharField(blank=True, choices=[('1', '健康保険組合'), ('2', '協会けんぽ（全国健康保険協会）'), ('3', '各種共済組合'), ('4', '国民健康保険'), ('5', '国民健康保険組合（長けん国保）'), ('6', '後期高齢者医療制度'), ('7', '船員保険（全国健康保険協会）'), ('8', '-')], max_length=100, null=True, verbose_name='健康保険')),
                ('HIlast4digits', models.CharField(blank=True, max_length=100, null=True, verbose_name='健康保険下4桁')),
                ('file1', models.FileField(blank=True, default='\\Soensv\\共有フォルダ\\新しいフォルダー', null=True, upload_to='', verbose_name='Link1健康保険')),
                ('pensionInsurance', models.CharField(blank=True, choices=[('1', '国民年金'), ('2', '厚生年金'), ('3', '-')], max_length=100, null=True, verbose_name='年金保険')),
                ('file2', models.FileField(blank=True, null=True, upload_to='', verbose_name='Link2年金保険')),
                ('employmentinsurance', models.CharField(blank=True, choices=[('1', '無'), ('2', '有'), ('3', '適用除外'), ('4', '-')], max_length=100, null=True, verbose_name='雇用保険')),
                ('EIlast4digits', models.CharField(blank=True, max_length=100, null=True, verbose_name='雇用保険下4桁')),
                ('file3', models.FileField(blank=True, null=True, upload_to='', verbose_name='Link3雇用保険')),
                ('retirementCooperation', models.CharField(blank=True, choices=[('1', '有'), ('2', '無'), ('3', '-')], max_length=100, null=True, verbose_name='建退協')),
                ('file4', models.FileField(blank=True, null=True, upload_to='', verbose_name='Link4建退協')),
                ('file6', models.FileField(blank=True, null=True, upload_to='', verbose_name='Link6技能講習')),
                ('file7', models.FileField(blank=True, null=True, upload_to='', verbose_name='Link免許')),
                ('driverLicence_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='自動車免許番号')),
                ('file8', models.FileField(blank=True, null=True, upload_to='', verbose_name='Link自動車免許証')),
                ('dateOfAdmission', models.DateField(blank=True, null=True, verbose_name='入場年月日')),
                ('file9', models.FileField(blank=True, null=True, upload_to='', verbose_name='Link9')),
                ('file10', models.FileField(blank=True, null=True, upload_to='', verbose_name='Link10')),
                ('constractionPermit', models.CharField(blank=True, choices=[('1', '建築工事業'), ('2', '内装仕上工事業'), ('3', '-')], max_length=100, null=True, verbose_name='建設業許可業種')),
                ('constractionPermit_chuji', models.CharField(blank=True, choices=[('1', '大臣'), ('2', '知事'), ('3', '-')], max_length=100, null=True, verbose_name='建設業許可_大臣・知事')),
                ('constractionPermit_ippan', models.CharField(blank=True, choices=[('1', '特定'), ('2', '一般'), ('3', '-')], max_length=100, null=True, verbose_name='建設業許可_特定・一般')),
                ('constractionPermit_nendo', models.CharField(blank=True, max_length=100, null=True, verbose_name='建設業許可_年度')),
                ('constractionPermit_num', models.CharField(blank=True, max_length=100, null=True, verbose_name='建設業許可_番号')),
                ('constractionPermit_gat', models.DateField(blank=True, null=True, verbose_name='建設業許可_取得年月日')),
                ('file5', models.FileField(blank=True, null=True, upload_to='', verbose_name='Link5')),
                ('contractDay', models.DateField(blank=True, null=True, verbose_name='工事契約日')),
                ('firstActionDay', models.DateField(blank=True, null=True, verbose_name='請負開始工期')),
                ('finishActionDay', models.DateField(blank=True, null=True, verbose_name='請負終了工期')),
                ('contractionDetail', models.CharField(blank=True, max_length=100, null=True, verbose_name='工事内容')),
                ('No_1_specific_skill_foreigner', models.CharField(blank=True, choices=[('1', '無'), ('2', '有'), ('3', '-')], max_length=100, null=True, verbose_name='一号特定技能外国人')),
                ('foreignWorker', models.CharField(blank=True, choices=[('1', '無'), ('2', '有'), ('3', '-')], max_length=100, null=True, verbose_name='外国人建設就労者')),
                ('foreignIntern', models.CharField(blank=True, choices=[('1', '無'), ('2', '有'), ('3', '-')], max_length=100, null=True, verbose_name='外国人技能実習生')),
                ('carryonMachine', models.CharField(blank=True, choices=[('1', '電動ｸﾞﾗｲﾝﾀﾞｰ'), ('2', '電動ﾄﾞﾘﾙ'), ('3', 'ｺﾝﾌﾟﾚｯｻｰ'), ('4', 'アーク溶接機'), ('5', '-')], max_length=100, null=True, verbose_name='持込機械')),
                ('mobileCrane', models.CharField(blank=True, max_length=100, null=True, verbose_name='移動式ｸﾚｰﾝ･車両系建設機械')),
                ('dangerous', models.CharField(blank=True, max_length=100, null=True, verbose_name='危険物OR有機溶剤OR特定化学物質')),
                ('licence', models.ManyToManyField(to='reimex.LicenceModel')),
                ('mvehicle', models.ManyToManyField(to='actualSpot.Vehicle')),
                ('skillTraning', models.ManyToManyField(to='reimex.SkillTraningModel')),
                ('specialEducation', models.ManyToManyField(to='reimex.SpecialEducationModel')),
            ],
            options={
                'verbose_name_plural': 'そうえんメンバー',
            },
        ),
    ]
