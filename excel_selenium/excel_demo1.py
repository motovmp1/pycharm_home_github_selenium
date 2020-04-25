import openpyxl


book = openpyxl.load_workbook("/home/elsys/Desktop/Teste/pycharm_home_github_selenium/excel_selenium/pythondemo.xlsx")
# This is make active
sheet = book.active

cell = sheet.cell(row=1, column=2)

print(cell.value)

# write into cell
sheet.cell(row=2, column=2).value = "Vinicius"

cell2 = sheet.cell(row=2, column=2)
print(cell2)
print(cell2.value)

