#使用array创建数组

#   1.导入numpy模块
import numpy as np
#   2.使用array函数创建一维数组，结果是一个ndarray对象
arr = np.array([1,2,3,4])
print(arr)
print(type(arr))
#   3.使用array函数创建二维数组，结果是一个ndarray对象
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
print(type(arr))
#   4.使用array函数创建三维数组，结果是一个ndarray对象
arr = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(arr)
print(type(arr))
#   5.array函数中dtype的使用 -- 强制转换数组内部元素的数据类型
d = np.array([3,4,5],dtype=float)
print(d)
print(type(d))
#   6.ndim指定列表的维度,使用原有内容按照一定规则构建n维数组
d = np.array([1,2,3],ndmin=3,dtype=float)
print(d)