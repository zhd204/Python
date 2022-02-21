import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from pprint import pprint
import os

fb_pass = os.environ["FBPASS"]
user_email = os.environ["EMAIL"]

chrome_driver_path = "/Users/admin/Documents/python/udemy_100_days_of_Code/Python/development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://tinder.com/")
time.sleep(2)

login_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a")
login_btn.click()
time.sleep(2)

login_w_FB_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button")
login_w_FB_btn.click()
time.sleep(2)

base_window = driver.window_handles[0]
if len(driver.window_handles) > 1:
    fb_login_window = driver.window_handles[1]
    driver.switch_to.window(fb_login_window)

email_text = driver.find_element(By.CSS_SELECTOR, "#loginform #email_container #email")
email_text.send_keys(user_email)

pass_text = driver.find_element(By.CSS_SELECTOR, "#loginform #pass")
pass_text.send_keys(fb_pass)

fb_login_btn = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input")
fb_login_btn.click()
time.sleep(5)


driver.switch_to.window(base_window)
accept_cookie_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/button")
accept_cookie_btn.click()
time.sleep(2)

allow_loc_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[3]/button[1]")
allow_loc_btn.click()
time.sleep(2)

enable_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[3]/button[1]")
enable_btn.click()
time.sleep(15)

# nope_btn = driver.find_element(By.XPATH, '//*[@id="u-1510067323"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[5]/div/div[2]/button')

while True:
    time.sleep(4)
    try:
        nope_btn = driver.find_element(By.XPATH,
                                       '//*[@id="u-1510067323"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[5]/div/div[2]/button')
        nope_btn.click()
    except selenium.common.exceptions.NoSuchElementException:
        continue


