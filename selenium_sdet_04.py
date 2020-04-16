# This is a github selenium with pycharm - Test all elements for second time
import time
import sys
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

password_user = (driver.find_element_by_xpath("//input[@name='password']"))

username.send_keys("tutorial")
time.sleep(1)
password_user.send_keys("tutorial")

driver.find_element_by_xpath("//input[@name='login']").click()


print(driver.title)

for time1 in range(1, 70, 1):
    print(time1,  end='. ', flush=True)
    time.sleep(1)
    time1 += 1
    if driver.title == "Find a Flight: Mercury Tours:":
        break

radio_btn_round_trip = driver.find_element_by_xpath("//body//b//input[1]")
print("")
print("Radio button is round trip")
print(radio_btn_round_trip.is_selected())

# This is close only one window
print("Finished the testing....")
driver.close()

# quit command can close all the browsers at the same time
