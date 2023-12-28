from keys import *
import requests

api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_config = {
    "query": input("Tell me which exercises you did. ")
}

response =  requests.post(url=api_endpoint, json=exercise_config, headers=headers)
print(response.text)