import requests
import os
import datetime
from utils import select_day

TOKEN = os.environ.get("PIXELA_API")
USERNAME = "masscircle"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
    "thanksCode": "ThisIsThanksCode"
}
# create an user
# response_create_user = requests.post(url=pixela_endpoint, json=user_params)
# print(response_create_user.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Exercise Tacking",
    "unit": "minutes",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# create a graph
# response_create_graph = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response_create_graph.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

yesterday = select_day(1)
# yesterday = datetime(year=2021, month=12, day=30)
pixel_params = {
    "date": yesterday,
    "quantity": "30",
    "optionalData": "{\"type\": \"elliptical\"}"
}
# create a pixel
# response_add_pixel = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response_add_pixel.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday}"

pixel_update_params = {
    "quantity": "40",
}
# update a pixel
response_update_pixel = requests.put(url=pixel_update_endpoint, json=pixel_update_params, headers=headers)
print(response_update_pixel.text)

# delete a user
# response_delete_user = requests.delete(url="https://pixe.la/v1/users/zhd204", headers=headers)
# print(response_delete_user.text)
