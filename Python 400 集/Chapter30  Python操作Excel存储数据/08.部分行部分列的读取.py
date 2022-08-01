import openpyxl
wb = openpyxl.load_workbook("work_book_excel.xlsx")
ws =wb.active
print("使用切片的方式进行对部分行部分列的获取")

cell_range = ws["A2:D4"]#在这里可以手动设置从哪里切片到哪里
for r in cell_range:
    for c in r:
        print(c.value,end="\t")
    print()