import requests
import os
import json
import datetime as dt

# -------------------------------request exercise information from nutritionix.com----------------------------
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

authentication_info = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
# authentication_str = json.dumps(authentication_info)
# print(authentication_str)
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
q_text = input("Which exercises did you do?")
exercise_parameters = {
    "query": q_text,
    "gender": "male",
    "weight_kg": 83.25,
    "height_cm": 183,
    "age": 40
}

exercise_response = requests.post(url=exercise_endpoint, json=exercise_parameters, headers=headers)
result = exercise_response.json()
# result_str = json.dumps(result, indent=4)
print(result)

# -------------------------------add selected exercise information to google sheet via Sheety API-----------------------
# reference to basic authentication
# https://docs.python-requests.org/en/master/user/authentication/#basic-authentication
# reference to bear authentication
# https://stackoverflow.com/questions/29931671/making-an-api-call-in-python-with-an-api-that-requires-a-bearer-token
sheety_sheet_endpoint = "https://api.sheety.co/f7fabb8332b440cfc3ec74a0c6df78d6/workoutTracking/workouts"

today_date = dt.datetime.now().strftime("%m/%d/%Y")
now_time = dt.datetime.now().strftime("%X")
TOKEN = os.environ.get("BEARER_TOKEN")

row_content = {
    "workout": {
        "date": today_date,
        "time": now_time,
        "exercise": result["exercises"][0]["name"].title(),
        "duration": result["exercises"][0]["duration_min"],
        "calories": result["exercises"][0]["nf_calories"]
    }
}

headers = {
    "Authorization": f"Bearer {TOKEN}", # bearer authentication
    "Content-Type": "application/json"
}

add_row_response = requests.post(url=sheety_sheet_endpoint, json=row_content, headers=headers)
add_row_response.raise_for_status()
print(add_row_response.text)
