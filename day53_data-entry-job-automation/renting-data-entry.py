import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import selenium.common.exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from collections import namedtuple
from pprint import pprint
from utils import get_price, complete_link_address


CHROME_DRIVER_PATH = "/Users/admin/Documents/python/udemy_100_days_of_Code/Python/development/chromedriver"

Rental = namedtuple("Rental", ["address", "price", "link"])

email_address = os.environ.get("EMAIL")
email_password = os.environ.get("PASSWORD")

url = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.69219435644531%2C%22east%22%3A-122.17446364355469%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D'


class renting_data_entry:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.results = []

    def testing(self, n):
        for i in range(n):
            self.results.append(Rental(f"test_address{i}", f"{(i + 1) * 100}", f"https://test{i}.com"))

    def get_rental_property(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9"
        }
        response = requests.get(url=url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.select("article", class_="list-card-additional-attribution")
        for article in articles:
            try:
                address = article.div.address.text.strip()
                price = get_price(article.div.div.next_sibling.div.text.split(" ")[0].strip())
                link = complete_link_address(article.div.a.get("href").strip())
                self.results.append(Rental(address, price, link))
            except AttributeError as ex:
                print(ex)
                print(article)
                continue

        # Alternative is to run the soup twice like below
        # ul = soup.find("ul", class_="photo-cards photo-cards_wow photo-cards_short")
        # soup2 = BeautifulSoup(str(ul), "html.parser")
        # listings = soup2.find_all("article")
        # for listing in listings:
        #     pprint(listing)
        #     print("\n")

    def fill_form(self):
        self.driver.get(
            "https://docs.google.com/forms/d/e/1FAIpQLSdQNRfSZcVdqoZbqHqXs5A3lMrp8COeH4ysjjbECcO_G9XRTQ/viewform?usp=sf_link")
        time.sleep(3)

        if len(self.results):
            for rental in self.results:
                property_address_input = self.driver.find_element(By.XPATH,
                                                                  "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
                property_address_input.send_keys(rental.address)

                property_price_input = self.driver.find_element(By.XPATH,
                                                                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
                property_price_input.send_keys(rental.price)

                property_link_input = self.driver.find_element(By.XPATH,
                                                               "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
                property_link_input.send_keys(rental.link)
                time.sleep(3)

                submit_btn = self.driver.find_element(By.XPATH,
                                                      "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div")
                submit_btn.click()
                time.sleep(3)

                submit_another_link = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
                submit_another_link.click()
                time.sleep(3)

        self.driver.quit()
        # ****************comment out below code due to fail to login google account due to security settings**************
        #
        # signin_link = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[1]/div/div[4]/div/div/a[1]")
        # signin_link.click()
        # time.sleep(3)
        #
        # base_window = self.driver.window_handles[0]
        # if len(self.driver.window_handles) > 1:
        #     google_login_window = self.driver.window_handles[1]
        # self.driver.switch_to.window(google_login_window)
        #
        # email_input = self.driver.find_element(By.XPATH,
        #                                        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
        # email_input.send_keys(email_address)
        # time.sleep(3)
        #
        # next_btn = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button")
        # next_btn.click()
        # time.sleep(3)

        # password_input = self.driver.find_element(By.XPATH,
        #                                           "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
        # password_input.send_keys(email_password)
        # time.sleep(3)


rental = renting_data_entry()
rental.get_rental_property()
rental.fill_form()
