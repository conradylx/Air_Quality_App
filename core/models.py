from datetime import datetime

from django.db import models


class Forecast(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    description = models.CharField(max_length=10)
    pressure = models.FloatField()
    wind_speed = models.FloatField()
    air_quality = models.IntegerField()
    co = models.FloatField(default=0)
    no = models.FloatField(default=0)
    no2 = models.FloatField(default=0)
    o3 = models.FloatField(default=0)
    so2 = models.FloatField(default=0)
    pm2_5 = models.FloatField(default=0)
    pm10 = models.FloatField(default=0)
    nh3 = models.FloatField(default=0)
    date_and_time = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return '{} {}'.format(self.city, self.date_and_time)
