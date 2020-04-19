# This is a github selenium with pycharm - Test all elements for second time
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import excel_utilits
import openpyxl
from openpyxl.styles import Font, Color, Alignment, Border, Side, colors
from openpyxl.styles import PatternFill, colors
import loggind_file_1

red_background = PatternFill(bgColor=colors.RED)

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
    print(type(r))
    cell_color = ('C' + str(r))
    print(cell_color)
    print(cell_color)
    username = excel_utilits.read_data_file(path, "Sheet1", r, 1)
    password = excel_utilits.read_data_file(path, "Sheet1", r, 2)

    driver.find_element_by_xpath("//input[@name='userName']").send_keys(username)
    time.sleep(2)
    driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    time.sleep(2)
    driver.find_element_by_xpath("//input[@name='login']").click()
    time.sleep(35)

    if driver.title == "Find a Flight: Mercury Tours:":
        print(driver.title)
        print("Test is PASS")
        excel_utilits.write_data_file(path, "Sheet1", r, 3, "PASS")
        excel_utilits.change_cell_color_pass(path, "Sheet1", r, 3, "PASS", cell_color)
    else:
        print("Test is FAIL")
        excel_utilits.write_data_file(path, "Sheet1", r, 3, "FAIL")
        excel_utilits.change_cell_color_fail(path, "Sheet1", r, 3, "FAIL", cell_color)
        loggind_file_1.logger.critical("Fail to login in the step test")
    driver.find_element_by_link_text("Home").click()
    time.sleep(4)
# ***************************** End test case   *******************************************


#       *** Close session   ***
print("Close all navigator")
time.sleep(5)
driver.close()
