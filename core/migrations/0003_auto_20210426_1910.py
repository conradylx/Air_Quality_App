# Generated by Django 3.2 on 2021-04-26 17:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_forecast_date_and_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='forecast',
            name='co',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='forecast',
            name='nh3',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='forecast',
            name='no',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='forecast',
            name='no2',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='forecast',
            name='o3',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='forecast',
            name='pm10',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='forecast',
            name='pm2_5',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='forecast',
            name='so2',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='forecast',
            name='date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 26, 19, 10, 23, 929212)),
        ),
    ]
