#导入模块
import numpy as np
import matplotlib.pyplot as plt
#以函数 z=x²+y²为例
#建立步长为0.01，即每隔0.01取一个点
step = 0.01
x = np.arange(-10,10,step)
y = np.arange(-10,10,step)
#也可以用x = np.linspace(-10,10,100)表示从-10到10，分100份

#将原始数据变成网格数据形式
X,Y = np.meshgrid(x,y)
#写入函数，z是大写
Z = X**2+Y**2
#设置打开画布大小,长10，宽6
#plt.figure(figsize=(10,6))
#填充颜色，f即filled
plt.contourf(X,Y,Z)
#画等高线 这句话同上
#plt.contour(X,Y,Z)
plt.show()