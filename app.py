import requests
from pprint import pprint

API_key = "fa319b80e1aca8304e55d725ae8abf23"

ville = input("Veuillez entrer une ville: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_key+"&q="+ville

weather_data = requests.get(base_url).json()

pprint(weather_data)                                                                                       