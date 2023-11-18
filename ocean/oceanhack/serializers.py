from rest_framework import serializers
from .models import WeatherData

class OceanSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = ['unique_id', 'datetime', 'tempmax', 'tempmin', 'temp', 'precip', 'precipprob', 'precipcover',
                  'windspeed', 'winddir', 'windgust', 'solarradiation', 'solarenergy', 'uvindex']
        