import openpyxl

wb =openpyxl.load_workbook("excelTest.xlsx")

#获取所有工作表的名称
print(wb.sheetnames)

#获取当前正在使用(active状态的)的workbook对象
print(wb.active)

#获取当前正在使用(active状态的)的workbook对象名称
print(wb.active.title)

#通过工作簿获取所有sheet工作表对象
for i in wb:
    print(i.title)#获取所有工作表的名称