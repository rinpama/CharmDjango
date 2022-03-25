# Generated by Django 3.2.7 on 2021-11-08 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actualSpot', '0004_auto_20211108_1842'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gcontractor',
            options={'verbose_name_plural': 'ｾﾞﾈｺﾝ会社'},
        ),
        migrations.AddField(
            model_name='aspot',
            name='constractionDetail',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ｾﾞﾈ工事内容'),
        ),
        migrations.AddField(
            model_name='aspot',
            name='contractDay',
            field=models.DateField(blank=True, null=True, verbose_name='ｾﾞﾈ請負契約日'),
        ),
        migrations.AddField(
            model_name='gcontractor',
            name='FaxNumber',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Fax番号'),
        ),
        migrations.AlterField(
            model_name='aspot',
            name='X',
            field=models.IntegerField(default='2', verbose_name='X次'),
        ),
        migrations.AlterField(
            model_name='aspot',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='現場住所'),
        ),
        migrations.AlterField(
            model_name='aspot',
            name='firstSubcontractor',
            field=models.CharField(default='株式会社\u3000装苑', max_length=50, verbose_name='現在1次 装苑 として'),
        ),
        migrations.AlterField(
            model_name='aspot',
            name='spotName',
            field=models.CharField(default='必須', max_length=50, verbose_name='現場名'),
        ),
        migrations.AlterField(
            model_name='aspot',
            name='superVisor',
            field=models.CharField(default='必須', max_length=50, verbose_name='現場所長名'),
        ),
        migrations.AlterField(
            model_name='gcontractor',
            name='gName',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='ｾﾞﾈｺﾝ会社名'),
        ),
    ]
