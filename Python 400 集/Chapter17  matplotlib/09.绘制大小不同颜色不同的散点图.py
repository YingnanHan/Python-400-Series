#导入模块
import matplotlib.pyplot as plt
import numpy as np

#绘制08中类似的图形
#创建 x y
np.random.seed(0)#设置执行多次得到的随机数组都是同样的
x = np.random.rand(100)
y = np.random.rand(100)
#生成100个大小模式
size = np.random.rand(100)*1000
#生成100种不同的颜色
color = np.random.rand(100)
#绘制散点图
plt.scatter(x,y,s=size,c=color,alpha=0.7)#alpha参数设定了透明度
plt.show()

#值得注意的是：点的个数和颜色的个数要相一致
#              点的个数和点的大小的个数可以不同
#              如果有n个点m种颜色或者大小(n>m)那么第k个点是m%k号颜色 也就是按规则循环获取相应的大小