# Generated by Django 4.0.1 on 2022-03-04 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Show', '0012_alter_assoenm_assmanager_alter_assoenm_assmember_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assoenm',
            name='actualspot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actualspot', to='Show.actualspotm'),
        ),
    ]
