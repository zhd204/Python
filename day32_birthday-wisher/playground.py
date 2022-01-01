# import smtplib
#
# my_email = "zhd204.testing@gmail.com"
# password = "Rockwell@123"
#
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="zhd204.testing@yahoo.com",
#                         msg="Subject:Hello Again!\n\nThis is the body of my email.")


import datetime as dt

now = dt.datetime.now()
print(now)