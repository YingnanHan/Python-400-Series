#mean函数用来求解一个数组的算数平均值

#一维数组的情形
import numpy as np
a = np.arange(5)
print(a)
print("算数平均值为",np.mean(a))

#二维数组的情形  要通过axis指定轴
a = np.arange(1,13).reshape(3,4)
print(a)
print("垂直方向的算数平均值",np.mean(a,axis=0))
print("水平方向的算数平均值",np.mean(a,axis=1))
