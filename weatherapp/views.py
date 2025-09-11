from django.shortcuts import render, HttpResponse
import requests
import datetime
import json 
# Create your views here.
def home(request):
    if 'city' in request.POST:  # check if user submitted a city
        city = request.POST['city']
    else:
        city = 'indore'  # default city

    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': '1d2c0181907197316ef0c053ca1a45c3',  # your API key
        'units': 'metric'
    }

    response = requests.get(url, params=params).json()

    # Extract some data from the API response
    data = {
        'city': city,
        'temperature': response['main']['temp'],
        'feels_like' : response['main']['feels_like'],
        'pressure' : response['main']['pressure'],
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
        'time': datetime.datetime.now()
    }

    return render(request, 'weatherapp/search.html', {'weather': data})
