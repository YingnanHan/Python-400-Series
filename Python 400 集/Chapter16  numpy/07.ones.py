#ones创建指定大小的数组，数组元素以1来填充

#导入numpy模块
import numpy as np

def onesTest():
    #直接创建
    z = np.ones(5)
    print(z)
    #指定类型创建
    n = np.ones(5,dtype=float)
    print(n)
    #指定规模创建数组
    s = np.ones((3,4),dtype=int)
    print(s)


onesTest()