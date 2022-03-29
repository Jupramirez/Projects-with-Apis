from pickle import APPEND
import requests
from datetime import datetime




APP_ID = "595e4725"
API_KEY = "d71b17011caa4e66e960343c7db45f79"

url_nutrition_stats = "https://trackapi.nutritionix.com/v2/natural/exercise"

config_nutrition = {
    "query": "Ran 2 miles and walked for 3km."
}

headers = {
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
    "x-remote-user-id":"0"
}

response = requests.post(url=url_nutrition_stats,json=config_nutrition,headers=headers)
data_excercise = response.json()

# print(response.url)



url_excercises_row = "https://api.sheety.co/3c85e49cf2c9724c6563c7437bbf1b46/wrokoutTracking/workouts"

for excercise in data_excercise["exercises"]:
    today = datetime.now()
    date_complete = today.strftime("%d/%m/%Y")
    date_time = today.strftime("%X")
    sheet_inputs= {
        "workout" : {
        "date":date_complete,
        "time":date_time,
        "exercise":excercise["name"].title(),
        "duration":excercise["duration_min"],
        "calories":excercise["nf_calories"]
    }}
    
    response = requests.post(url=url_excercises_row,json=sheet_inputs)
    

