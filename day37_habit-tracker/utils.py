import datetime


def select_day(delta_day: int) -> str:
    now = datetime.datetime.now()
    day = (now - datetime.timedelta(days=delta_day)).strftime("%Y%m%d")  # yyyymmdd as string
    return day

