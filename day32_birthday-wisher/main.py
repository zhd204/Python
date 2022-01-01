import datetime as dt
import random
import smtplib

quote_list = []
with open("quotes.txt") as file:
    quote_list = file.read().split("\n")

date_of_week = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
now = dt.datetime.now()

my_email = "zhd204.testing@gmail.com"
password = "Rockwell@123"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="hellogeli@gmail.com",
                        msg=f"Subject:Good {date_of_week[now.weekday()]}!\n\n{random.choice(quote_list)}")
