# Generated by Django 3.2.7 on 2021-11-09 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reimex', '0004_auto_20211109_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='soenmodel',
            name='driverLicence_number',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='自動車免許番号'),
        ),
        migrations.AlterField(
            model_name='soenmodel',
            name='file8',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Link自動車免許証'),
        ),
    ]
