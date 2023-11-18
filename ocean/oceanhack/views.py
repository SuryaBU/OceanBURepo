#from django.shortcuts import render

# Create your views here.
#from django.http import JsonResponse
#from .models import WeatherData
#from .serializers import OceanSerializer

#def weather_list(request):
#    oceandetails = WeatherData.objects.all()
#    serializer = OceanSerializer(oceandetails, many=True)
#    return JsonResponse(serializer.data, safe=False)

#def weather_list(request):
    # Specify the datetime range you want to filter
  #  start_date = '2023-01-01'
   # end_date = '2023-02-01'

    # Filter WeatherData objects based on datetime range
  #  oceandetails = WeatherData.objects.filter(datetime__range=[start_date, end_date])

    # Serialize the specified fields
 #   serializer = OceanSerializer(oceandetails, many=True)

    # Extract only the required fields from the serialized data
#    serialized_data = [{'datetime': item['datetime'], 'temp': item['temp']} for item in serializer.data]

#    return JsonResponse(serialized_data, safe=False)
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .models import WeatherData
from .serializers import OceanSerializer

@require_GET
@csrf_exempt
def weather_list(request):
    # Get parameters from the request
    start_date_str = request.GET.get('start_date')
    end_date_str = request.GET.get('end_date')
    additional_field = request.GET.get('additional_field')

    # Check if start_date and end_date are provided
    if not (start_date_str and end_date_str):
        return JsonResponse({'error': 'start_date and end_date are required'}, status=400)

    # Validate and convert start and end dates to datetime objects
    try:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
    except ValueError:
        return JsonResponse({'error': 'Invalid date format'}, status=400)

    # Filter WeatherData objects based on datetime range
    oceandetails = WeatherData.objects.filter(datetime__range=[start_date, end_date])

    # Serialize the specified fields
    serializer = OceanSerializer(oceandetails, many=True)

    # Extract only the required field from the serialized data
    serialized_data = [{additional_field: item[additional_field]} for item in serializer.data]

    return JsonResponse(serialized_data, safe=False)

