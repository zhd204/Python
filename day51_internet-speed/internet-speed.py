import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 940
PROMISED_UP = 10
CHROME_DRIVER_PATH = "/Users/admin/Documents/python/udemy_100_days_of_Code/Python/development/chromedriver"

username = os.environ.get("TWITTER-USERNAME")
password = os.environ.get("TWITTER-PASSWORD")

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get("https://twitter.com/")
time.sleep(3)

signin_btn = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a")
signin_btn.click()
time.sleep(3)

username_input = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input")
username_input.send_keys(username)
time.sleep(3)

next_btn = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]")
next_btn.click()
time.sleep(3)

password_input = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input")
password_input.send_keys(password)
time.sleep(3)

login_btn = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div")
login_btn.click()
time.sleep(3)