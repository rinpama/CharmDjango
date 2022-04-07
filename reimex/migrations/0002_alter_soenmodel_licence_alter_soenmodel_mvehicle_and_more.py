# Generated by Django 4.0.1 on 2022-04-07 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actualSpot', '0003_alter_aspot_xsubcontractor_and_more'),
        ('reimex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soenmodel',
            name='licence',
            field=models.ManyToManyField(blank=True, null=True, to='reimex.LicenceModel'),
        ),
        migrations.AlterField(
            model_name='soenmodel',
            name='mvehicle',
            field=models.ManyToManyField(blank=True, null=True, to='actualSpot.Vehicle'),
        ),
        migrations.AlterField(
            model_name='soenmodel',
            name='skillTraning',
            field=models.ManyToManyField(blank=True, null=True, to='reimex.SkillTraningModel'),
        ),
        migrations.AlterField(
            model_name='soenmodel',
            name='specialEducation',
            field=models.ManyToManyField(blank=True, null=True, to='reimex.SpecialEducationModel'),
        ),
    ]
