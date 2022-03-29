import requests


OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "f2fa8a4170da636f3ddb4310288c193b"

weather_params = {
    "lat": 4.6534649,
    "lon": -74.0836453,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour in weather_slice:
    num = hour["weather"][0]["id"]
    if(num < 700):
        will_rain = True


if will_rain:
    print("LLeva sombrilla")