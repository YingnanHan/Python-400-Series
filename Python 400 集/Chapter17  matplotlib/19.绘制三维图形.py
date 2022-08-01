import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

X = np.linspace(-10,10,1000)
Y = np.linspace(-10,10,1000)
#绘制三维图像之前，需要将X,Y处理成平面上的点也就是平面展示
X,Y = np.meshgrid(X,Y)
Z = np.array(np.power(X,2)+np.power(Y,2))
fig = plt.figure()
#创建一个Axe3D的子图放在fig画布上
axe = Axes3D(fig)
axe.plot_surface(X,Y,Z)#使用plot_trisurf绘制三维图形
plt.show()