from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from django.db.models import Prefetch
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ContinentSerializer, CountrySerializer, CitySerializer, WeatherSerializer, TimeWeatherSerializer, TimeWeather6Serializer, TimeWeather9Serializer, TimeWeather12Serializer, TimeWeather15Serializer, TimeWeather20Serializer, TimeWeather23Serializer
from .models import Continent, Country, City, DateWeather, TimeWeather, TimeWeather6, TimeWeather9, TimeWeather12, TimeWeather15, TimeWeather20, TimeWeather23

# Create your views here.


class ContinentListAll(APIView):
    def get(self, request, format=None):
        continents = Continent.objects.all()
        serializer = ContinentSerializer(continents, many=True)
        return Response(serializer.data)


class ContinentList(viewsets.ViewSet):
    def list(self, request, continent_name=None):
        queryset = Continent.objects.all()
        user = get_object_or_404(queryset, continent_name=continent_name)
        serializer = ContinentSerializer(user)
        return Response(serializer.data)

    def retrieve(self, request, continent_name=None, conutry_name=None, city_name=None):
        if conutry_name and city_name:

            queryset = Continent.objects.filter(continent_name=continent_name).prefetch_related(
                Prefetch("country", queryset=Country.objects.filter(
                    conutry_name=conutry_name).prefetch_related(
                    Prefetch('city', queryset=City.objects.filter(city_name=city_name)))
                )
            )
        else:
            queryset = Continent.objects.filter(continent_name=continent_name).prefetch_related(
                Prefetch("country", queryset=Country.objects.filter(
                    conutry_name=conutry_name))
            )

        serializer = ContinentSerializer(queryset, many=True)

        return Response(serializer.data)


class CountryList(APIView):
    def get(self, request, format=None):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)


class CityList(APIView):
    def get(self, request, format=None):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)


class WeatherList(APIView):
    def get(self, request, format=None):
        date_weathers = DateWeather.objects.all()
        serializer = WeatherSerializer(date_weathers, many=True)
        return Response(serializer.data)

class TimeWeatherList(APIView):
    def get(self, request, format=None):
        timeweather = TimeWeather.objects.all()
        serializer = TimeWeatherSerializer(timeweather, many=True)
        return Response(serializer.data)

class TimeWeather6List(APIView):
    def get(self, request, format=None):
        timeweather6 = TimeWeather6.objects.all()
        serializer = TimeWeather6Serializer(timeweather6, many=True)
        return Response(serializer.data)

class TimeWeather9List(APIView):
    def get(self, request, format=None):
        timeweather9 = TimeWeather9.objects.all()
        serializer = TimeWeather9Serializer(timeweather9, many=True)
        return Response(serializer.data)
    
class TimeWeather12List(APIView):
    def get(self, request, format=None):
        timeweather12 = TimeWeather12.objects.all()
        serializer = TimeWeather12Serializer(timeweather12, many=True)
        return Response(serializer.data)
    
class TimeWeather15List(APIView):
    def get(self, request, format=None):
        timeweather15 = TimeWeather15.objects.all()
        serializer = TimeWeather15Serializer(timeweather15, many=True)
        return Response(serializer.data)
    
class TimeWeather20List(APIView):
    def get(self, request, format=None):
        timeweather20 = TimeWeather20.objects.all()
        serializer = TimeWeather20Serializer(timeweather20, many=True)
        return Response(serializer.data)
    
class TimeWeather23List(APIView):
    def get(self, request, format=None):
        timeweather23 = TimeWeather23.objects.all()
        serializer = TimeWeather23Serializer(timeweather23, many=True)
        return Response(serializer.data)

def home(request):
  return HttpResponse("Home page")

# def get_continent(request):
#   cont_list = Continent.objects.all()
#   context = {'continents' : cont_list}
#   return render(request, 'weather_app/continents.html', context=context)
