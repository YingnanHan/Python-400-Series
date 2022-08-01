import openpyxl
from openpyxl.chart import PieChart,Reference

#准备数据
data = [
    ["Pie","Sold"],
    ["Apple",50],
    ["Cherry",30],
    ["Pumpkin",40],
    ["Chocolate",30]
]

#将数据写入到excel当中
#创建工作簿
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Pie Chart"

for row in data:
  ws.append(row)

#开始绘图以及计算工作
pie_chart = PieChart()
pie_chart.title = "Pies solds by catagory"

catogory = Reference(ws,min_col=2,min_row=2,max_row=5,max_col=1)#指定目录数据在excel的存储范围
data     = Reference(ws,min_col=2,min_row=2,max_row=5,max_col=2)#指定目录数据在excel的存储范围
#指定目录以及数据的对应关系并且放到饼图中
pie_chart.add_data(data)  #先添加数据在设置分类 不然图标就会失效
pie_chart.set_categories(catogory)

#在excel sheet中添加饼状图，并且设置位置
ws.add_chart(pie_chart,"D3")

#保存工作簿
wb.save("piechart.xlsx")