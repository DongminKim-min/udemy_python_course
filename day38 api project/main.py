import requests
import datetime
import os

APP_ID = "a2a9ecc7"
API_KEY = "c7e03ac77bed4017c2dc1126656d8b0f"
SHEET_ENDPOINT = "https://api.sheety.co/3348d8c65592389624cb85196ab4f228/myWorkouts/workouts"
USERNAME = "DongminKim"
PASSWORD = "Dave1004@"

DATE = datetime.datetime.today().strftime("%m/%d/%Y")
TIME = datetime.datetime.now().strftime("%H:%M:%S")

nutri_end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"


nutri_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

nutri_params = {
    # "query": input("Tell me which exercise you did. "),
    "query": "I did 45 minutes chest bodybuilding workout in a gym.",
    "gender": "male",
    "weight_kg": 65,
    "height_cm": 168,
    "age": 23
}

nutri_response = requests.post(url=nutri_end_point, json=nutri_params, headers=nutri_headers)
data = nutri_response.json()["exercises"][0]
exercise = data["user_input"]
duration = str(data["duration_min"])
calories = str(data["nf_calories"])

sheet_params = {
                   "workout": {
                       "date": DATE,
                       "time": TIME,
                       "exercise": exercise,
                       "duration": duration,
                       "calories": calories
                   }
                }

sheet_response = requests.post(url= SHEET_ENDPOINT, json=sheet_params,
                               auth=(USERNAME, PASSWORD))
print(sheet_response.json())