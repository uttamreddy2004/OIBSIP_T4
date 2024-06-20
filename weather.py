import requests
def get_weather(api_key, city):
    url = "http://api.openweathermap.org/data/2.5/weather?"
    parameters = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(url, params=parameters)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['name'],'temperature': data['main']['temp'],'description': data['weather'][0]['description'],'humidity': data['main']['humidity'],'wind_speed': data['wind']['speed']
        }
        return weather
    else:
        return f"Error: {response.status_code}, {response.json()['message']}"
api_key = '0aba5bd9a1e1fe778c3f53be1f34c68c'
city=input("ENTER CITY NAME :")
weather_data = get_weather(api_key, city)
if isinstance(weather_data, dict):
    print(f"CITY: {weather_data['city']}")
    print(f"TEMPERATURE: {weather_data['temperature']}°C")
    print(f"WEATHER: {weather_data['description']}")
    print(f"HUMIDITY: {weather_data['humidity']}%")
    print(f"WIND SPEED: {weather_data['wind_speed']} m/s")
else:
    print(weather_data)
