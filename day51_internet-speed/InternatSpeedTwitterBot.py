import os

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 940
PROMISED_UP = 10
CHROME_DRIVER_PATH = "/Users/admin/Documents/python/udemy_100_days_of_Code/Python/development/chromedriver"

username = os.environ.get("TWITTER-USERNAME")
password = os.environ.get("TWITTER-PASSWORD")


class InternetSpeedTwitterBot:
    def __init__(self):
        self.down_spd = 0
        self.up_spd = 0
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        go_btn = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a")
        go_btn.click()

        wait = True
        while wait:
            try:
                time.sleep(10)
                back_to_result_btn = self.driver.find_element(By.XPATH,
                                                              "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/div[2]/a")
                back_to_result_btn.click()
                wait = False
            except selenium.common.exceptions.ElementNotInteractableException as ex:
                continue

        time.sleep(3)
        self.down_spd = float(self.driver.find_element(By.CSS_SELECTOR, ".download-speed").text)
        self.up_spd = float(self.driver.find_element(By.CSS_SELECTOR, ".upload-speed").text)

    def tweet_at_provider(self):

        self.driver.get("https://twitter.com/")
        time.sleep(3)

        signin_btn = self.driver.find_element(By.XPATH,
                                              "/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a")
        signin_btn.click()
        time.sleep(3)

        username_input = self.driver.find_element(By.XPATH,
                                                  "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input")
        username_input.send_keys(username)
        time.sleep(3)

        next_btn = self.driver.find_element(By.XPATH,
                                            "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]")
        next_btn.click()
        time.sleep(3)

        password_input = self.driver.find_element(By.XPATH,
                                                  "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input")
        password_input.send_keys(password)
        time.sleep(3)

        login_btn = self.driver.find_element(By.XPATH,
                                             "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div")
        login_btn.click()
        time.sleep(3)

        message_input = self.driver.find_element(By.XPATH,
                                                 "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div")
        message_input.send_keys(f"Here we go. My FIOS is running at {self.down_spd}Mbps/{self.up_spd}Mbps!")
        time.sleep(3)

        tweet_btn = self.driver.find_element(By.XPATH,
                                             "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]")
        tweet_btn.click()
        time.sleep(10)

        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
print(bot.down_spd)
print(bot.up_spd)
time.sleep(3)
bot.tweet_at_provider()
