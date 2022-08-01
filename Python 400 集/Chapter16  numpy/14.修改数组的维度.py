#使用reshape来修改数组的维度


###方法一 reshape作为对象的方法

#导入numpy模块
import numpy as np
#通过numpy.reshape将一位数组修改为二维数组或者三维数组
a = np.arange(24)
print(a)
#将一维数组修改为二维数组
b = a.reshape(4,6)#修改为4x6的数组
print(b)
b = a.reshape((6,4))#以元组作为参数修改为4x6的元组
print(b)
#将一维数组修改为三维数组 (2,3,4)
c = a.reshape((2,3,4))
print(c)

###方法二 reshape作为np下的函数模块
bb  =  np.reshape(a,(3,8))
print(bb)
bb = np.reshape(a,(4,3,2))
print(b)

###将多维数组修改为一维数组
a = bb.reshape(24)#这种方法必须要提前计算出bb里面有多少个数字
print(a)
a = bb.reshape(-1)#默认代表bb里面的元素数目
print(a)

#通过ravel，flatten函数将多维数组转换为一维数组
#① ravel
a = bb.ravel()
print(a)

#② flatten
a = bb.flatten()
print(a)
