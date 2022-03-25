# Generated by Django 3.2.7 on 2021-11-04 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reimex', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mostRecent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Xx', models.IntegerField(blank=True, null=True, verbose_name='X次')),
                ('recentName', models.CharField(blank=True, max_length=20, null=True, verbose_name='上位会社名')),
                ('postalCode', models.CharField(blank=True, max_length=20, null=True, verbose_name='郵便番号')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='現住所')),
                ('telephoneNumber', models.CharField(blank=True, max_length=20, null=True, verbose_name='電話番号')),
            ],
            options={
                'verbose_name_plural': 'ゼネ･直近上位会社',
            },
        ),
        migrations.CreateModel(
            name='Aspot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checking', models.BooleanField(default=False, verbose_name='選択フラグ')),
                ('spotName', models.CharField(default='作業員名簿必須', max_length=50, verbose_name='現場名')),
                ('superVisor', models.CharField(default='作業員名簿必須', max_length=50, verbose_name='現場所長名')),
                ('firstSubcontractor', models.CharField(default='作業員名簿必須', max_length=50, verbose_name='一次協力会社名')),
                ('X', models.IntegerField(default='作業員名簿', verbose_name='X次')),
                ('XSubcontractor', models.CharField(default='作業員名簿必須', max_length=50, verbose_name='X次協力会社名')),
                ('kanaName', models.CharField(default='ｶﾀｶﾅ現場名', max_length=50, verbose_name='カナ入力現場名')),
                ('address', models.CharField(default='sasebo', max_length=50, verbose_name='住所')),
                ('firstActionDay', models.DateField(blank=True, null=True, verbose_name='全体開始工期')),
                ('finishActionDay', models.DateField(blank=True, null=True, verbose_name='全体終了工期')),
                ('members', models.ManyToManyField(to='reimex.SoenModel')),
                ('mostRecent', models.ManyToManyField(to='actualSpot.mostRecent')),
            ],
            options={
                'verbose_name_plural': '現場名',
            },
        ),
    ]
