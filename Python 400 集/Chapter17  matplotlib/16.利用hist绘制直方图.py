import numpy as np
import matplotlib.pyplot as plt

#生成1000个标准正态分布的随机数
x = np.random.randn(1000)
#plt.hist(x)
#使用bins属性修改柱形的宽度
plt.hist(x,bins=100)#表示每十个数据绘制在同一个柱内部
plt.show()