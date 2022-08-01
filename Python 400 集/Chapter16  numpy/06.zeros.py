#zeros创建指定大小的数组，数组元素以0来填充

#导入numpy模块
import numpy as np

def zerosTest():
    #直接创建
    z = np.zeros(5)
    print(z)
    #指定类型创建
    n = np.zeros(5,dtype=float)
    print(n)
    #指定规模创建数组
    s = np.zeros((3,4),dtype=int)
    print(s)


zerosTest()