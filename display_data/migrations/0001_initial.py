# Generated by Django 2.1.3 on 2018-12-21 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdultData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveSmallIntegerField()),
                ('workclass', models.CharField(max_length=100)),
                ('fnlwgt', models.IntegerField()),
                ('education', models.CharField(max_length=100)),
                ('education_num', models.IntegerField()),
                ('marital_status', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=100)),
                ('relationship', models.CharField(max_length=100)),
                ('race', models.CharField(max_length=100)),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('capital_gain', models.IntegerField()),
                ('capital_loss', models.IntegerField()),
                ('hours_per_week', models.IntegerField()),
                ('native_country', models.CharField(max_length=100)),
                ('salary_per_anum', models.CharField(choices=[('<=50K', '<=50K'), ('>50K', '>50K')], max_length=100)),
            ],
        ),
    ]
