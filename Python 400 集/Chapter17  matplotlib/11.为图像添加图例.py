#导入模块
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)
y = np.linspace(0,10,100)

#手动设置样式  并且使用label参数来设置图例 默认位置在左上角
#图例的位置可以通过loc属性来设置
plt.plot(x,y+0,"--g",label="--g")#表示使用短横杠表示曲线 颜色为绿色
plt.plot(x,y+1,"-.r",label="-.r")#表示使用 -. 表示曲线 颜色为红色
plt.plot(x,y+2,":b",label=":b")#表示使用:表示曲线 颜色为蓝色
plt.plot(x,y+3,".k",label=".k")#表示使用.表示曲线 颜色为暗色
plt.plot(x,y+4,",c",label=",c")#表示使用,表示曲线 颜色为青色
plt.plot(x,y+5,"*y",label="*y")#表示使用*表示曲线 颜色为黄色

plt.legend(loc = "upper left",fancybox=True,framealpha=1,shadow=True,borderpad=1)
#plt.legend()
plt.show()