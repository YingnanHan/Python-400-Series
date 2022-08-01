#使用arrange创建数组
#导入numpy
import numpy as np
'''
range的使用
range(start,end,step) [start,end)

'''
#使用range创建列表
a = list(range(1,10))
print(a)
a = list(range(10))#默认从零开始，步长为1
print(a)
a = list(range(1,10,3))#指定步长为3
print(a)

#使用arange创建数组
a = np.arange(1,11)#创建一个范围[1,11)步长为1的数组
print(a)

#人为设置步长step参数
a = np.arange(1,100,step=5)
print(a)

#使用dtype属性
#c = np.arange([1,2,3,4,5,6],dtype=float)
#print(c)