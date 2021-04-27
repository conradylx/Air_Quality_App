from datetime import datetime

import requests
from django.shortcuts import render
from django.views.generic import TemplateView

from core.models import Forecast


def concatenate_data_from_apis(city, api_key):
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    weather_to_json = requests.get(weather_url.format(city)).json()

    lon = weather_to_json["coord"]["lon"]
    lat = weather_to_json["coord"]["lat"]
    pollution_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"
    pollution_to_json = requests.get(pollution_url.format(lon, lat)).json()

    return weather_to_json, pollution_to_json


def save_api_data(context, pollution_to_json):
    Forecast(city=context['city'],
             temperature=context['temperature'],
             description=context['description'],
             pressure=context['pressure'],
             wind_speed=context['wind_speed'],
             air_quality=context['air_quality'],
             co=pollution_to_json["list"][0]["components"]["co"],
             no=pollution_to_json["list"][0]["components"]["no"],
             no2=pollution_to_json["list"][0]["components"]["no2"],
             o3=pollution_to_json["list"][0]["components"]["o3"],
             so2=pollution_to_json["list"][0]["components"]["so2"],
             pm2_5=pollution_to_json["list"][0]["components"]["pm2_5"],
             pm10=pollution_to_json["list"][0]["components"]["pm10"],
             nh3=pollution_to_json["list"][0]["components"]["nh3"],
             date_and_time=datetime.now().replace(microsecond=0)).save()


def index(request):
    api_key = ''

    if request.method == 'POST':
        try:
            city = request.POST.get('city')

            weather_to_json, pollution_to_json = concatenate_data_from_apis(city, api_key)
            context = {
                'city': city,
                'temperature': round(weather_to_json["main"]["temp"]),
                'description': weather_to_json["weather"][0]["description"],
                'pressure': weather_to_json["main"]["pressure"],
                'wind_speed': weather_to_json["wind"]["speed"],
                'air_quality': pollution_to_json["list"][0]["main"]['aqi']
            }

            request.session['one'] = context['city']
            print(request.session['one'])
            save_api_data(context, pollution_to_json)
        except:
            context = {}
    else:
        context = {}

    return render(request, 'core/index.html', context)


class ChartView(TemplateView):
    template_name = "core/charts.html"

    def get_context_data(self, **kwargs):
        city = self.request.session.get('one')
        context = super().get_context_data(**kwargs)
        context["qs"] = Forecast.objects.filter(city=city).order_by('-date_and_time')[:8][::-1]
        context["city_name"] = city
        print(context["qs"])
        return context
