#barh函数用来绘制水平方向的柱状图
#bar函数用来绘制垂直方向的柱状图

import matplotlib.pyplot as plt
import numpy as np

#生成x y
np.random.seed(0)
x = np.arange(5)
y = np.random.randint(-5,5,5)
#讲画布分为1行2列 在第一个区域绘制bar
plt.subplot(1,2,1)
plt.bar(x,y,color="red")
#在0处添加蓝色的线条
plt.axhline(0,color="blue",linewidth=2)
################################
plt.subplot(1,2,2)
plt.barh(x,y,color="green")
plt.axvline(0,color="red",linewidth=2)
plt.show()