import requests
from datetime import datetime
from dateutil import tz, parser

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# print(data)
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (latitude, longitude)
# print(iss_position)

MY_LAT = 40.213280
MY_LNG = -77.008034
parameter = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()

data = response.json()

sunrise_str = data["results"]["sunrise"]
sunset_str = data["results"]["sunset"]

from_zone = tz.tzutc()
to_zone = tz.tzlocal()

sunrise_utc = parser.isoparse(sunrise_str)
sunset_utc = parser.isoparse(sunset_str)

sunrise_local = sunrise_utc.astimezone(to_zone)
sunset_local = sunset_utc.astimezone(to_zone)

print(f"sunrise time is {sunrise_local}, sunset time is {sunset_local}")
