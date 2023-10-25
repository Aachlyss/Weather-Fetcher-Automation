import requests
import math

API_KEY = "ccfdb4b005b85109bebed09a341cb674"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


city = input("Enter a city name: ")
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather']
    print(weather)
    temperature = data['main']['temp']
    min_temperature = data['main']['temp_min']
    max_temperature = data['main']['temp_max']

    temperature -= 273.15
    min_temperature -= 273.15
    max_temperature -= 273.15

    print("Curremt Temperature: " + f"{math.ceil(temperature)}")
    print("Curremt Min Temperature: " + f"{math.ceil(min_temperature)}")
    print("Curremt Max Temperature: " + f"{math.ceil(max_temperature)}")

else:
    print("An error occurred")