from keys import *
import requests
from datetime import datetime

today = datetime.now()

api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/42aa639590991ae9d9debec840ee3761/workoutTracker/workouts"


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_config = {
    "query": input("Tell me which exercises you did. ")
}

response = requests.post(url=api_endpoint, json=exercise_config, headers=headers)
# print(response.text)
result = response.json()

sheety_config = {
    "workout": {
        "date": today.strftime("%Y%m%d"),
        "time": today.strftime("%X"),
        "exercise": result["exercises"][0]["name"].title(),
        "duration": result["exercises"][0]["duration_min"],
        "calories": result["exercises"][0]["nf_calories"]
    }
}

# print(sheety_config)

sheet_response = requests.post(sheety_endpoint, json=sheety_config)
print(sheet_response.text)