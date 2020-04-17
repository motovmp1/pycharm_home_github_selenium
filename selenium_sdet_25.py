import openpyxl
import time

path = "/home/elsys/Desktop/Teste/pycharm_home_github_selenium/readexcel.xlsx"

workbook = openpyxl.load_workbook(path)

# sheet = workbook.get_sheet_by_name("Sheet1")

sheet = workbook.active

