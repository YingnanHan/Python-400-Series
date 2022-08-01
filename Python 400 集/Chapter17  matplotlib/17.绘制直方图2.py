import numpy as np
import matplotlib.pyplot as plt

#生成1000个指定均值与方差的随机数
x = np.random.normal(0,0.8,1000)#生成1000个均值为0方差为0.8的数据
y = np.random.normal(-2,1,1000)
z = np.random.normal(3,2,1000)
#plt.hist(x)

#使用bins属性修改柱形的宽度
plt.hist(x,bins=100)#表示每十个数据绘制在同一个柱内部
plt.hist(y,bins=100)
plt.hist(z,bins=100)
plt.show()