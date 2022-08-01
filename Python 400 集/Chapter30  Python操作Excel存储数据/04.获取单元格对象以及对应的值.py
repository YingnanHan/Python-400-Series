import openpyxl

wb = openpyxl.load_workbook("work_book_excel.xlsx")
#获取当前活跃的sheet对象
ws = wb.active
#根据单元格名称获取A4位置处的对象以及内容
obj = ws["A4"]
print(obj)  #打印对象信息
print(obj.value)#打印单元格对应的值
print(obj.column)#获取单元格的列信息
print(obj.row)#获取单元格的行信息  这里得到的是第几行而不是字母
