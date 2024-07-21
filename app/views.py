import requests
from django.shortcuts import render
from django.http import JsonResponse
from .models import City, WeatherForecast
from .forms import CityForm

def get_weather_forecast(city_name):
    api_url = f"https://api.open-meteo.com/v1/forecast?current_weather=true&q={city_name}"
    response = requests.get(api_url)
    data = response.json()
    temperature = data["current_weather"]["temperature"]
    wind_speed = data["current_weather"]["windspeed"]
    return temperature, wind_speed

def index(request):
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data["city_name"]
            city, created = City.objects.get_or_create(name=city_name)
            temperature, wind_speed = get_weather_forecast(city_name)
            WeatherForecast.objects.create(city=city, temperature=temperature, wind_speed=wind_speed)
            return render(request, "app/weather_forecast.html", {"city_name": city_name, "temperature": temperature, "wind_speed": wind_speed})
    else:
        form = CityForm()
    return render(request, "app/index.html", {"form": form})

def history(request):
    cities = City.objects.all()
    return render(request, "app/history.html", {"cities": cities})

def api_history(request):
    cities = City.objects.all()
    data = [{"city": city.name, "count": WeatherForecast.objects.filter(city=city).count()} for city in cities]
    return JsonResponse(data, safe=False)


def autocomplete(request):
    term = request.GET.get("term")
    cities = City.objects.filter(name__icontains=term)
    data = [{"label": city.name, "value": city.name} for city in cities]
    return JsonResponse(data, safe=False)