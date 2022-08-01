#subplot函数的功能是将画布分区，将图形绘制到指定区域
import numpy as np
import matplotlib.pyplot as plt

#将画布分区，将图形绘制到指定的区域
##  分区效果
##      1      2
##      3      4

#创建0-10中100个等差数列
x = np.linspace(-50,50,5000)
y = np.sin(x)
#对画布进行分区然后绘制正弦曲线
plt.subplot(2,2,1)#这句话的意思是 讲画布划分为四个区域sin函数绘制在第一个区域
#修改x，y轴的坐标范围 这句话一定要放在subplot后面
plt.xlim(-20,20)
plt.ylim(-1,1)
plt.plot(x,y)

#创建0-10中100个等差数列
x = np.linspace(0,10,100)
y = np.cos(x)
#对画布进行分区然后绘制余弦曲线
plt.subplot(2,2,2)#这句话的意思是 讲画布划分为四个区域cos函数绘制在第二个区域
plt.plot(x,y)


plt.show()