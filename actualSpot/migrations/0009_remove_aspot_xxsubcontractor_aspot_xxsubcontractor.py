# Generated by Django 4.0.1 on 2022-07-13 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reimex', '0005_alter_soenmodel_mvehicle'),
        ('actualSpot', '0008_alter_aspot_gcontractor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aspot',
            name='XxSubcontractor',
        ),
        migrations.AddField(
            model_name='aspot',
            name='XxSubcontractor',
            field=models.ManyToManyField(to='reimex.SoenModel'),
        ),
    ]
