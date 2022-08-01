import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5,6,7,8,9,10]
y = [1,-2,3,-4,5,-6,7,-8,9,-10]

x = np.array(x)
y = np.array(y)

plt.axhline(0,color="blue",linewidth=3)
#对y值大于0的设置蓝色，小于0的设置绿色
v = plt.bar(x,y,color="blue")
for bar,height in zip(v,y):
    if height>0:
        bar.set(color="green")#根据情况调用set函数进行设置
plt.show()