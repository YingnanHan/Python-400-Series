import openpyxl
from openpyxl.chart import BarChart
from openpyxl.chart import Reference

rows = [
    ["Numbers","Batch1","Batch2"],
    [2,40,30],
    [3,40,25],
    [4,30,24],
    [5,26,28],
    [6,32,21],
    [7,28,31]
]

#创建工作簿
wb = openpyxl.Workbook()
ws = wb.create_sheet("barChart")
ws.title = "Bar Chart"
#将数据写入到excel当中
for row in rows:
    ws.append(row)

#绘制图形
bar_chart = BarChart()
bar_chart.type = 'bar'  #设置垂直柱状图  bar水平柱状图
bar_chart.title = "BarChart" #设置名称
bar_chart.style = 10 #设置图像的大小以及类型
bar_chart.x_axis.title = "Sample length(mm)"    #设置X轴的坐标名称
bar_chart.y_axis.title = "Test number"          #设置Y轴的坐标名称

catagory = Reference(ws,min_row=2,max_row=7,min_col=1,max_col=1) #设置目录
data = Reference(ws,min_row=1,max_row=7,min_col=2,max_col=3) #设置数据
bar_chart.add_data(data,titles_from_data=True) #在图中添加数据  第二个参数表示标题信息是从数据中获取
bar_chart.set_categories(catagory) #在图中设置目录

ws.add_chart(bar_chart,"E1") #将图片放在某一个确定的位置
#保存工作簿
wb.save("barchart.xlsx")