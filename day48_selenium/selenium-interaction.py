from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "/Users/admin/Documents/python/udemy_100_days_of_Code/Python/development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org")
# article_count = driver.find_element_by_css_selector("#articlecount a")  # Dedicated by methods are deprecating
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")   # Recommend to use find_element(s) and By class
print(article_count.text)
# time.sleep(3)
# # navigate to the href link included in the article count tag
# article_count.click()

# all_portals = driver.find_element_by_link_text("All portals")
all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# time.sleep(2)
# all_portals.click()

search = driver.find_element(By.NAME, "search")
time.sleep(2)
search.send_keys("Python")
search.send_keys(Keys.ENTER)
time.sleep(5)
driver.quit()
