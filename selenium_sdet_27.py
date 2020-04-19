# This is a github selenium with pycharm - Test all elements for second time
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("https://www.amazon.in/")
# This is a title of the page
driver.implicitly_wait(6)
time.sleep(1)
driver.maximize_window()
time.sleep(1)
print(driver.title)

# Test case inside the browser

cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

# adding new cookie to the browser
cookie_new = {'name': 'Mycookie', 'value': '12345678'}
driver.add_cookie(cookie_new)

cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

# Deleting the coookie
driver.delete_cookie('Mycookie')

cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

# Close all navigator
print("Finished Testing ....")
time.sleep(4)
driver.close()
