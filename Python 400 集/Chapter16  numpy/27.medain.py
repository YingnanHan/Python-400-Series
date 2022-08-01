#median函数用来求解数组中的中位数

#一维数组的情形
import numpy as np
a = np.arange(5)
print(a)
print("中位数为",np.median(a))

#二维数组的情形  要通过axis指定轴
a = np.arange(1,13).reshape(3,4)
print(a)
print("垂直方向的中位数",np.median(a,axis=0))
print("水平方向的中位数",np.median(a,axis=1))
