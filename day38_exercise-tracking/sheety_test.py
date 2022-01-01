import requests
import json

retrieve_endpoint = "https://api.sheety.co/f7fabb8332b440cfc3ec74a0c6df78d6/workoutTracking/workouts/"
# response = requests.get(url=retrieve_endpoint)
# response.raise_for_status()
# data = response.json()
# print(data)

add_endpoint = "https://api.sheety.co/f7fabb8332b440cfc3ec74a0c6df78d6/workoutTracking/workouts/"
row_content = {
    "workout": {
        "date": "12/31/2021",
        "time": "16:30:00",
        "exercise": "elliptical",
        "duration": "30",
        "calories": "150"
    }
}
headers = {
    "Content-Type": "application/json"
}
# response = requests.post(url=add_endpoint, json=row_content)
# response.raise_for_status()
# print(response.text)

i = 4
while i > 2:
    delete_response = requests.delete(url=f"{add_endpoint}/{i}")
    delete_response.raise_for_status()
    print(delete_response.text)
    i -= 1
