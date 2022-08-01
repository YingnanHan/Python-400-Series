#数组的水平方向的拼接

'''
A  1 2 3        B   1 2 3
   4 5 6            4 5 6

水平拼接后得到的结果是
1 2 3 1 2 3
4 5 6 4 5 6
'''

#导入numpy
import numpy as np
#创建两个数组
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[11,12,13],[14,15,16]])
print(a)
print(b)
#使用hstack对数组进行水平拼接
res = np.hstack([a,b])
print(res)