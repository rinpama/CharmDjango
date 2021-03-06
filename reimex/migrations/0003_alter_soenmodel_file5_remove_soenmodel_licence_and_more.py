# Generated by Django 4.0.1 on 2022-05-21 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reimex', '0002_alter_soenmodel_licence_alter_soenmodel_mvehicle_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soenmodel',
            name='file5',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Link5雇用・職長・特別教育'),
        ),
        migrations.RemoveField(
            model_name='soenmodel',
            name='licence',
        ),
        migrations.AddField(
            model_name='soenmodel',
            name='licence',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='reimex.licencemodel'),
        ),
        migrations.RemoveField(
            model_name='soenmodel',
            name='skillTraning',
        ),
        migrations.AddField(
            model_name='soenmodel',
            name='skillTraning',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='reimex.skilltraningmodel'),
        ),
        migrations.RemoveField(
            model_name='soenmodel',
            name='specialEducation',
        ),
        migrations.AddField(
            model_name='soenmodel',
            name='specialEducation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='reimex.specialeducationmodel'),
        ),
    ]
