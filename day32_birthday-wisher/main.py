import datetime as dt
import os
import random
import smtplib

quote_list = []
with open("day32_birthday-wisher/quotes.txt") as file:
    quote_list = file.read().split("\n")

date_of_week = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
now = dt.datetime.now()

my_email = os.environ.get("TESTING_EMAIL")
password = os.environ.get("EMAIL_PASSWORD")

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="testing01.python@gmail.com",
                        msg=f"Subject:Good {date_of_week[now.weekday()]}!\n\n{random.choice(quote_list)}")
