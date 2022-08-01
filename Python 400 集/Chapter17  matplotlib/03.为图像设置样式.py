#导入matplot模块
import matplotlib.pyplot as plt

#准备 x y
x = [1,2,3,4,5]
y = [1,4,9,16,25]
#绘制图像

#使用 linewidth 设置图像的属性
plt.plot(x,y,linewidth=5)
#为坐标轴添加相应的名称
plt.xlabel("x")
plt.ylabel("y=x²")
#为图像添加标题 并且设置中文支持
plt.rcParams['font.sans-serif'] = ['SimHei']#用来正常显示中文标签
plt.title("一个折线统计图")
plt.show()