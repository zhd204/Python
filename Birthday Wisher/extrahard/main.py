##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random
from os import listdir
from os.path import isfile, join
import smtplib

username = "zhd204.testing@gmail.com"
password = "Rockwell@123"


def send_email(receiver_address, email_body):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=username, password=password)
        connection.sendmail(from_addr=username,
                            to_addrs=receiver_address,
                            msg=email_body)


# 1. Update the birthdays.csv

# 1a. Generate a list of the birthday letter templates.
path = "letter_templates"
files = [path + "/" + f for f in listdir(path) if isfile(join(path, f))]

# 2. Check if today matches a birthday in the birthdays.csv
birthdays_df = pd.read_csv("birthdays.csv")
birthdays_list = birthdays_df.to_dict("records")

today = dt.datetime.now()

matched_list = [birthday for birthday in birthdays_list
                if birthday["month"] == today.month and birthday["day"] == today.day]
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if len(matched_list) > 0:
    filepath = random.choice(files)
    with open(filepath) as f:
        letter = f.read()

    for birthday in matched_list:
        letter = letter.replace("[NAME]", birthday["name"])
        email_msg = "Subject:Happy Birthday!\n\n" + letter
        send_email(birthday['email'], email_msg)
else:
    print("No matched birthday!")

# 4. Send the letter generated in step 3 to that person's email address.
# def send_email():
#     pass
