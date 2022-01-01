import smtplib
import time

import requests
from datetime import datetime
from dateutil import tz, parser

# To find your latitude and longitude https://www.latlong.net/
MY_LAT = 40.213280  # Your latitude
MY_LONG = -77.008034  # Your longitude


def iss_in_place(lat, lng):
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if abs(lat - iss_latitude) <= 5 and abs(lng - iss_longitude) <= 5:
        return True


def is_dark(lat, lng):
    parameters = {
        "lat": lat,
        "lng": lng,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise_str = data["results"]["sunrise"]
    sunset_str = data["results"]["sunset"]

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()

    sunrise_utc = parser.isoparse(sunrise_str)
    sunset_utc = parser.isoparse(sunset_str)

    # All three times are in local time now
    sunrise_local = sunrise_utc.astimezone(to_zone)
    sunset_local = sunset_utc.astimezone(to_zone)
    time_now = datetime.now()

    if time_now.hour > sunset_local.hour or time_now.hour < sunrise_local.hour:
        return True


while True:
    time.sleep(60)
    if iss_in_place(MY_LAT, MY_LONG) and is_dark(MY_LAT, MY_LONG):
        my_email = "zhd204.testing@gmail.com"
        password = "Rockwell@123"

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="zhd204@gmail.com",
                                msg=f"Subject:Look up!\n\nISS is passing through!")
