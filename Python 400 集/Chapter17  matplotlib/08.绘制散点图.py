#导入模块
import matplotlib.pyplot as plt
import numpy as np
#生成0-10之间100个等差数
x = np.linspace(0,10,100)
sin_y = np.sin(x)
#绘制正弦曲线
plt.scatter(x,sin_y)
plt.show()