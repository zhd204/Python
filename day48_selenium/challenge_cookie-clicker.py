from decimal import Decimal

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from pprint import pprint
from collections import namedtuple
import math


def click_cookie(driver_object, seconds):
    cookie = driver_object.find_element(By.ID, "cookie")
    start = time.perf_counter()
    end = start
    while (end - start) <= seconds:
        cookie.click()
        end = time.perf_counter()


# Generate list out of index error
# def store_items(driver_object):
#     store_list = driver_object.find_elements(By.CSS_SELECTOR, "#store div")
#     # Below line works better. Refer to https://stackoverflow.com/questions/59637048/how-to-find-element-by-part-of-its-id-name-in-selenium-with-python
#     # store_ls = driver.find_elements(By.CSS_SELECTOR, "[id^='buy']")
#     store = []
#     store_ls = store_list[:-1]
#     for item in store_list:  # ignore the last incomplete item in the store list
#         try:
#             print(item.text + "\n")
#             if item.text != "":
#                 name = item.get_attribute("id")
#                 price_strings = (item.text.split(' - ')[1]).split('\n')
#                 price_string = price_strings[0]
#                 price = int(price_string.strip().replace(',', ''))
#                 enabled = not (item.get_attribute("class"))
#                 store.append(StoreItem(name, price, enabled))
#         except IndexError as ex:
#             print(ex)
#             print(store)
#             continue
#     return store

def store_items(driver_object):
    # id_list = driver_object.find_elements(By.CSS_SELECTOR, "#store div") # generate id="", which could be the issue of getting list out of index
    # Below line works better. Refer to https://stackoverflow.com/questions/59637048/how-to-find-element-by-part-of-its-id-name-in-selenium-with-python
    id_list = driver.find_elements(By.CSS_SELECTOR, "[id^='buy']")
    ids = [item.get_attribute("id") for item in id_list]
    enabled = [not (bool(item.get_attribute("class"))) for item in id_list]

    price_list = driver_object.find_elements(By.CSS_SELECTOR, "#store div b")
    prices = [int(item.text.split(" - ")[1].replace(",", "")) for item in price_list if item.text]
    store = [StoreItem(ids[index], prices[index], enabled[index]) for index in range(len(prices))]
    return store


def select_item(store_ls: list, current_money):
    print(store_ls)
    store_ls.reverse()
    print(store_ls)
    for item in store_ls:
        if item.enabled and current_money >= item.price:
            print(item)
            print("\n")
            return item


def get_current_total(driver_object):
    current_total = Decimal(driver_object.find_element(By.ID, "money").text.replace(",", ""))
    return current_total


def purchase_item(driver_object, selected_item):
    item = driver_object.find_element(By.ID, selected_item.id)
    item.click()


StoreItem = namedtuple("StoreItem", ["id", "price", "enabled"])
run_time = int(input("Please enter expected run time in minutes:\n"))
chrome_driver_path = "/Users/admin/Documents/python/udemy_100_days_of_Code/Python/development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
store_items(driver)

start = time.perf_counter()
end = start
while end - start <= run_time * 60:
    click_cookie(driver, 10)
    dt = store_items(driver)
    current_cookies = get_current_total(driver)
    purchase_item(driver, select_item(dt, current_cookies))

print(f"Final count of the cookies is: {get_current_total(driver)}")
