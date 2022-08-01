'''
numpy.split 函数沿特定的轴将数组分割为子数组，格式如下：
numpy.split(ary, indices_or_sections, axis)
参数说明：
ary：被分割的数组
indices_or_sections：如果是一个整数，就用该数平均切分，如果是一个数组，为沿轴切分的
位置。
axis：沿着哪个维度进行切向，默认为 0，横向切分。为 1 时，纵向切分。
'''

import numpy as np
x = np.arange(1,9)

#调用split函数进行分割
a = np.split(x,4)#将数组平均分成4分
print(a)
#传递数组按位置分割
a = np.split(x,[3,5])#将数组划分为0 1 2 3| 4  5 | 6 7 8的形式
print(a)

print("-----------------------")
#二维数组的分割
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(a)
print("axis=0 垂直方向 平均分割")#上下分
r,w = np.split(a,2,axis=0)
print(r)
print(w)
print("-----------------------")
print("axis=1 水平方向 平均分割")#左右分
l,r = np.split(a,[2],axis=1)
print(l)
print(r)
print("-----------------------")
#按位置分割 上下分割
r,w,k  =  np.split(a,[2,3],axis=0)
print(r)
print(w)
print(k)