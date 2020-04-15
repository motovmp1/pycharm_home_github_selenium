# This is a github selenium with pycharm - Test all elements for second time
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("http://www.newtours.demoaut.com/")
# This is a title of the page
time.sleep(1)
driver.maximize_window()
time.sleep(1)
print(driver.title)

# This is get URL of the page
time.sleep(1)
print(driver.current_url)

username = (driver.find_element_by_xpath("//input[@name='userName']"))

user_enable = username.is_enabled()
time.sleep(1)
user_display = username.is_displayed()

# Validation for user enable inside the web - page
assert user_enable is True
if user_enable is True:
    print("PASS user enable")
else:
    print("Fail")
time.sleep(2)
# Validation for user displayed inside the web page
assert user_display is True
if user_display is True:
    print("PASS user display")
else:
    print("Fail")

time.sleep(5)

# This is close only one window
print("Finished the testing")
driver.close()

# quit command can close all the browsers at the same time
