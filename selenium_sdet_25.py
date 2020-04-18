import openpyxl
import time

path = "/home/elsys/Desktop/Teste/pycharm_home_github_selenium/readexcel_write.xlsx"

workbook = openpyxl.load_workbook(path)

# sheet = workbook.get_sheet_by_name("Sheet1")

sheet = workbook.active

for r in range(1, 6):
    for c in range(1, 4):
        sheet.cell(row=r, column=c).value = "welcome"

workbook.save(path)
