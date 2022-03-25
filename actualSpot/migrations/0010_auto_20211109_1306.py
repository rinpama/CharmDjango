# Generated by Django 3.2.7 on 2021-11-09 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actualSpot', '0009_auto_20211109_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mostrecent',
            name='constractionPermit',
            field=models.CharField(blank=True, choices=[('1', '建築工事業'), ('2', '内装仕上工事業'), ('3', '-')], max_length=100, null=True, verbose_name='建設業許可業種'),
        ),
        migrations.AlterField(
            model_name='mostrecent',
            name='constractionPermit_chuji',
            field=models.CharField(blank=True, choices=[('1', '大臣'), ('2', '知事'), ('3', '-')], max_length=100, null=True, verbose_name='建設業許可_大臣・知事'),
        ),
        migrations.AlterField(
            model_name='mostrecent',
            name='constractionPermit_ippan',
            field=models.CharField(blank=True, choices=[('1', '特定'), ('2', '一般'), ('3', '-')], max_length=100, null=True, verbose_name='建設業許可_特定・一般'),
        ),
    ]
