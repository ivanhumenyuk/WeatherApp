import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    appid = '56f5d6a8cb459fb7cd51a885db42af07'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid #&units=metric преобразовует кельвины цельсий

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities =[]

    for city in cities:
        response = requests.get(url.format(city.name)).json()  # готовый словарь, форматированный из json
        city_info = {
            'city': city.name,
            'temp': response['main']['temp'],
            'icon': response['weather'][0]['icon']
        }
        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}


    return render(request, 'weather/index.html', context)
    #по умолчанию все шаблоны ищуться и рендеряться в папке templates

