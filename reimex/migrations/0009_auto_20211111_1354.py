# Generated by Django 3.2.7 on 2021-11-11 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reimex', '0008_auto_20211111_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soenmodel',
            name='djgroup2',
            field=models.CharField(blank=True, default='装苑 or', max_length=100, null=True, verbose_name='所属(souen)'),
        ),
        migrations.AlterField(
            model_name='soenmodel',
            name='familyAdd',
            field=models.CharField(default='同上', max_length=100, verbose_name='家族連絡先'),
        ),
        migrations.AlterField(
            model_name='soenmodel',
            name='refer',
            field=models.CharField(default='内装工事', max_length=100, verbose_name='※1'),
        ),
    ]
