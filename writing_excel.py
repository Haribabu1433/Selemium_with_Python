import openpyxl

path = r"C:\Users\hpolicha\Documents\pyexcel\data1.xlsx"
workbook = openpyxl.load_workbook(path)
sheet = workbook.active                      #workbook.get_sheet_by_name("Sheet1")


for r in range(7,11):
    for c in range(1,5):
            sheet.cell(row=r,column=c).value = "hari"
workbook.save(path)