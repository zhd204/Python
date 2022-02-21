from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/admin/Documents/python/udemy_100_days_of_Code/Python/development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# # open a web browser with the link address
# driver.get("https://www.amazon.com")
# # close active the tab
# driver.close()
# # shut off the entire browser
# driver.quit()

# product_url = "https://www.amazon.com/Book-CODESYS-ultimate-Industrial-programming/dp/1737821400"
# driver.get(product_url)
# price = driver.find_elements(by="id", value="price")[0].text
# # price = driver.find_elements(By.CLASS_NAME, "a-size-base")
# print(price)
# driver.quit()

driver.get("https://python.org")
# search_bar = driver.find_element_by_name("q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))
#
# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)
#
# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)
#
# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

ls = driver.find_elements_by_css_selector(".event-widget .menu li")
# dt = {}
# for item in ls:
#     time, name = item.text.split("\n")
#     dt[ls.index(item)] = {"time": time, "name": name}
dt = {ls.index(item): {"time": item.text.split('\n')[0], "name": item.text.split('\n')[1]} for item in ls}
print(dt)

# dt = {ls.index(item): {"time": item.text.split('\n')[0]}, "name": item.text.split('\n')[1]}}
driver.quit()
