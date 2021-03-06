# Generated by Django 4.0.1 on 2022-04-07 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reimex', '0001_initial'),
        ('actualSpot', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aspot',
            name='XSubcontractor',
            field=models.ManyToManyField(blank=True, null=True, to='actualSpot.mostRecent'),
        ),
        migrations.AlterField(
            model_name='aspot',
            name='XxSubcontractor',
            field=models.ManyToManyField(blank=True, null=True, to='reimex.SoenModel'),
        ),
        migrations.AlterField(
            model_name='aspot',
            name='gContractor',
            field=models.ManyToManyField(blank=True, null=True, to='actualSpot.gContractor'),
        ),
    ]
