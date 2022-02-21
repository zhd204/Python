import smtplib

import requests
from bs4 import BeautifulSoup
import os

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
product_url = "https://www.amazon.com/Book-CODESYS-ultimate-Industrial-programming/dp/1737821400"
response = requests.get(url=product_url, headers=headers)
response.raise_for_status()


soup = BeautifulSoup(response.text, "lxml")
try:
    price = soup.find_all("span", class_="a-color-price", id="price")[0].text
    price_float = float(price.split("$")[1])
    print(price_float)

    title = soup.find_all("span", class_="a-size-extra-large", id="productTitle")[0].text
    print(title)
except IndexError as er:
    print(er)
    print("No matching item is found.")

my_email = os.environ.get("TESTING_EMAIL")
password = os.environ.get("EMAIL_PASSWORD")

target_price = 300.0

if price_float <= target_price:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="testing01.python@gmail.com",
                            msg=f"Subject:The Book is below {target_price}! Buy it!!!\n\n Title is {title} at {product_url}")
