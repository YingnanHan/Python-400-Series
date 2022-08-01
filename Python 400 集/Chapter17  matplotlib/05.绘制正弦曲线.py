import matplotlib.pyplot as plt
import numpy as np
#生成400点的坐标
x = np.linspace(-200,200,400)
y = np.sin(x)

#绘制正弦方程的曲线
plt.plot(x,y)

#保存图片到本地
plt.savefig("Sine.jpg")
plt.show()