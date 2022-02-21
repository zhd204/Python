import requests
import datetime


def response_data(url, params, **kwargs):
    request_response = requests.get(url=url, params=params)
    request_response.raise_for_status()
    return_data = request_response.json()
    return return_data


def select_day(time_series_daily_dict: dict, delta_day: int, date="") -> str:
    """select valid day defined by the delta_day (consider weekend case)"""
    now = datetime.datetime.now()
    valid_day = False
    day = ""

    while not valid_day:
        day = str((now - datetime.timedelta(days=delta_day)).date())  # yyyy-mm-dd as string
        if day in time_series_daily_dict.keys() and day != date:
            valid_day = True
        else:
            delta_day += 1

    return day
