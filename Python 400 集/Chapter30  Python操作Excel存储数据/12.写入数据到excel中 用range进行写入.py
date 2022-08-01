import openpyxl
wb =openpyxl.load_workbook("excelTest.xlsx")
ws = wb.create_sheet("使用range进行写入")

for i in range(41):#创建41行
    ws.append(range(1,16))#在每一行中写每一列

wb.save("excelTest.xlsx")