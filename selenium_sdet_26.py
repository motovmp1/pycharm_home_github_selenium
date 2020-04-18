# This is a github selenium with pycharm - Test all elements for second time
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import excel_utilits

driver = webdriver.Firefox()

driver.get("http://www.newtours.demoaut.com/")
# This is a title of the page
driver.implicitly_wait(10)
time.sleep(1)
driver.maximize_window()
time.sleep(1)
print(driver.title)

# This is get URL of the page
time.sleep(1)
print(driver.current_url)

# ********** Test Case ***********************************************************

# path from excel file
path = "/home/elsys/Desktop/Teste/pycharm_home_github_selenium/login_class_26.xlsx"

# number of rows that we have
numbers_rows = excel_utilits.get_row_count(path, "Sheet1")
print(numbers_rows)

for r in range(2, numbers_rows + 1):
    username = excel_utilits.read_data_file(path, "Sheet1", r, 1)
    password = excel_utilits.read_data_file(path, "Sheet1", r, 2)

    driver.find_element_by_xpath("//input[@name='userName']").send_keys("")
    time.sleep(2)
    driver.find_element_by_xpath("//input[@name='password']").send_keys("")
    time.sleep(2)
    driver.find_element_by_xpath("//input[@name='login']").click()

# ***************************** End test case   *******************************************


#       *** Close session   ***
print("Close all navigator")
time.sleep(5)
driver.close()
