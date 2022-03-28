# Generated by Django 4.0.1 on 2022-03-28 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actualSpot', '0001_initial'),
        ('reimex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='driver',
            field=models.ManyToManyField(to='reimex.SoenModel'),
        ),
        migrations.AddField(
            model_name='mostrecent',
            name='members',
            field=models.ManyToManyField(to='reimex.SoenModel'),
        ),
        migrations.AddField(
            model_name='mostrecent',
            name='vehicle',
            field=models.ManyToManyField(to='actualSpot.Vehicle'),
        ),
        migrations.AddField(
            model_name='aspot',
            name='XSubcontractor',
            field=models.ManyToManyField(to='actualSpot.mostRecent'),
        ),
        migrations.AddField(
            model_name='aspot',
            name='XxSubcontractor',
            field=models.ManyToManyField(to='reimex.SoenModel'),
        ),
        migrations.AddField(
            model_name='aspot',
            name='gContractor',
            field=models.ManyToManyField(to='actualSpot.gContractor'),
        ),
    ]
