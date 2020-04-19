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

driver.get("http://www.pavantestingtools.com/")

# This is a title of the page
time.sleep(1)
print(driver.title)

# This is get URL of the page
time.sleep(1)
print(driver.current_url)
