#concatenate 连接沿现有轴的数组序列
# axis=0 等效于 vstack  垂直堆叠数组  vertical
# axis=1 等效于 hstack  水平堆叠数组  horizontal

#导入numpy
import numpy as np
#创建两个数组
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[11,12,13],[14,15,16]])
print(a)
print(b)
print("--------------------------")
r1 = np.concatenate((a,b),axis=0)
r2 = np.concatenate((a,b),axis=1)
print(r1)
print(r2)
print("--------------------------")
#三维数组上的堆叠 axis 0 1 2
a = np.arange(1,13).reshape(1,2,6)
print(a,a.shape)
b = np.arange(101,113).reshape(1,2,6)
print(b,b.shape)
print("--------------------------")
#在三维数组上指定轴进行拼接
#0-axis
r1 = np.concatenate((a,b),axis=0)
print(r1)
#1-axis
r2 = np.concatenate((a,b),axis=1)
print(r2)
#2-axis
r3 = np.concatenate((a,b),axis=2)
print(r3)