import datetime as dt

today_date = dt.datetime.now().strftime("%m/%d/%Y")

now_time = dt.datetime.now().strftime("%X")

print(today_date, now_time)

time_iso = dt.datetime.now().time()
now_time = ((time_iso.hour + ((time_iso.minute + (time_iso.second / 60.0)) / 60.0)) / 24.0)

print(time_iso, now_time)