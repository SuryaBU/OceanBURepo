# import_weather_data.py
import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from oceanhack.models import WeatherData

class Command(BaseCommand):
    help = 'Import weather data from CSV file'

    def handle(self, *args, **options):
        with open('C:\\Users\\jrspr\\Downloads\\output_file.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                datetime_value = datetime.strptime(row.get('datetime', ''), '%m/%d/%Y')
                WeatherData.objects.create(
                    datetime=datetime_value,
                    tempmax=row['tempmax'],
                    tempmin=row['tempmin'],
                    temp=row['temp'],
                    precip=row['precip'],
                    precipprob=row['precipprob'],
                    precipcover=row['precipcover'],
                    windspeed=row['windspeed'],
                    winddir=row['winddir'],
                    solarradiation=row['solarradiation'],
                    windgust=row['windgust'],
                    solarenergy=row['solarenergy'],
                    uvindex=row['uvindex']
                    
                )
