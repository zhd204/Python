from decimal import Decimal

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from pprint import pprint
from collections import namedtuple


def click_cookie(driver_object, seconds):
    cookie = driver_object.find_element(By.XPATH, "/html/body/div/div[2]/div[15]/div[8]/div[1]")
    start = time.perf_counter()
    end = start
    while (end - start) <= seconds:
        cookie.click()
        end = time.perf_counter()


StoreItem = namedtuple("StoreItem", ["id", "price", "enabled"])
chrome_driver_path = "/Users/admin/Documents/python/udemy_100_days_of_Code/Python/development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")

