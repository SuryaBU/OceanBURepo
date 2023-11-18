# models.py

from django.db import models

class WeatherData(models.Model):
    datetime = models.DateField()  # Date/Time (GMT)
    tempmax = models.FloatField()
    tempmin = models.FloatField()
    temp = models.FloatField()
    precip = models.FloatField()
    precipprob = models.FloatField()
    precipcover = models.FloatField()
    windspeed = models.FloatField()  # Wind (m/s)
    winddir = models.FloatField()  # Wind Dir (deg)
    windgust = models.FloatField()  # Gust (m/s)
    solarradiation = models.FloatField()  # Solar (W/m^2)
    solarenergy = models.FloatField()
    uvindex = models.FloatField()  # UV (W/m^2)
    unique_id = models.AutoField(primary_key=True)  # Additional primary key


