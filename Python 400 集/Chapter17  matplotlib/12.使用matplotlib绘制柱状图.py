import numpy as np
import matplotlib.pyplot as plt

#创建x y 表示x年 的销量y
x = [1980,1985,1990,1995]
showX = ["1980年","1985年","1990年","1995年"]
y = [1000,3000,4000,5000]
#设置不出现中文乱码
plt.rcParams['font.sans-serif'] = 'SimHei'
#调用bar函数绘制柱状图
plt.bar(x,y,width=1.5)#width参数表示柱状图中的柱的宽度是原来的多少倍
#修改x坐标的值
plt.xticks(x,showX)#X坐标上的文字使用自定义字符，而不是系统生成的字符
#给x坐标 y坐标添加名称
plt.xlabel("年份")
plt.ylabel("销量")
#为图像添加标题
plt.title("销量随年份变化图像")
plt.show()