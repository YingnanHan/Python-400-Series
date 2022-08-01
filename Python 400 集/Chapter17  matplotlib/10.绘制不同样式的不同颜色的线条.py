#导入模块
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)
y = np.linspace(0,10,100)

#手动设置样式

plt.plot(x,y+0,"--g")#表示使用短横杠表示曲线 颜色为绿色
plt.plot(x,y+1,"-.r")#表示使用 -. 表示曲线 颜色为红色
plt.plot(x,y+2,":b")#表示使用:表示曲线 颜色为蓝色
plt.plot(x,y+3,".k")#表示使用.表示曲线 颜色为暗色
plt.plot(x,y+4,",c")#表示使用,表示曲线 颜色为青色
plt.plot(x,y+5,"*y")#表示使用*表示曲线 颜色为黄色

plt.show()