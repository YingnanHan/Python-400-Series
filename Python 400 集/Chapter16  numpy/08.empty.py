#empty方法用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组，里面的元素的值是之前内存的值
#导入numpy模块
import numpy as np

def emptyTest():
    #直接创建
    z = np.empty(5)
    print(z)
    #指定类型创建
    n = np.empty(5,dtype=float)
    print(n)
    #指定规模创建数组
    s = np.empty((3,4),dtype=int)
    print(s)


emptyTest()