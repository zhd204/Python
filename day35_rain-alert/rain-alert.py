import requests
import datetime
import os
from twilio.rest import Client

# OpenWeather account info
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ["OWM_API_KEY"]

# Twilio account info
account_sid = os.environ["ACCT_SID"]
auth_token = os.environ["AUTH_TOKEN"]

# parameters = {
#     "lat": 40.2143,
#     "lon": -77.0086,
#     "appid": api_key,
#     "exclude": "current,minutely,daily,alerts",
#     "units": "metric"
# }

# test with Halifax Canada
parameters = {
    "lat": 44.648766,
    "lon": -63.575237,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts",
    "units": "metric"
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()

hourly_ls = data["hourly"]
for item in hourly_ls:
    item["dt"] = datetime.datetime.fromtimestamp(item["dt"])
print(hourly_ls)

will_rain = False
for index in range(12):
    if will_rain:
        break
    else:
        n = len(hourly_ls[index]["weather"])
        for i in range(n):
            if hourly_ls[index]["weather"][i]["id"] < 700:
                will_rain = True
                break
print(will_rain)

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_="+16674010418",  # purchased/trial phone number from Twilio
        to="+17178142546"  # verified number with Twilio, in this case it is the phone number used via the registration.
    )
    print(message.status)
