#!/usr/bin/env python3
import urllib3
import json
import pygeoip
import maxminddb

__author__ = "matthew beerens"
__version__ = "0.1.0"
__license__ = "MIT"

API_KEY = "58a993196b7de1334f4cd18e09dd66e9"
KELIV = -273.15

def get_ip(http):
	return http.request('GET', 'https://api.ipify.org').data.decode('utf-8')

def get_weather_data(http,lat,lon):
	weather_request = 'https://api.openweathermap.org/data/2.5/weather?lat='+str(lat)+'&lon='+str(lon)+'&appid='+API_KEY
	# weather_request_n = 'https://api.openweathermap.org/data/2.5/weather?zip=2760,AU&appid='+API_KEY
	return http.request('GET', weather_request)

def get_location(http):
	reader = maxminddb.open_database('GeoLite2-City.mmdb')
	location = reader.get(str(get_ip(http)))
	lon = location['location']['longitude']
	lat = location['location']['latitude']
	reader.close()
	return [lon, lat]

def get_weather_icon(http, icon):
	return http.request('GET','http://openweathermap.org/img/w/'+str(icon)+'.png')

def get_weather():
	http = urllib3.PoolManager()
	location = get_location(http)
	weather = get_weather_data(http,location[1], location[0]).data
	weather = json.loads(weather)
	data = []
	data.append(weather['weather'])
	data.append(weather['main'])
	data.append(weather['wind'])
	data.append(get_weather_icon(http,data[0][0]['icon']))
	print(type(data[3]))
	return data