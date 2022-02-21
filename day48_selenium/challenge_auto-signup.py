from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "/Users/admin/Documents/python/udemy_100_days_of_Code/Python/development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://secure-retreat-92358.herokuapp.com/")
inp_fname = driver.find_element(By.NAME, "fName")
inp_fname.send_keys("Joe")
inp_lname = driver.find_element(By.NAME, "lName")
inp_lname.send_keys("Keiper")
inp_email = driver.find_element(By.NAME, "email")
inp_email.send_keys("JK@gmail.com")
btn_signup = driver.find_element(By.TAG_NAME, "button")
# btn_signup.send_keys(Keys.ENTER)
btn_signup.click()
time.sleep(3)
driver.quit()
