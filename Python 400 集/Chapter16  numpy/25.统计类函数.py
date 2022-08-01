'''
函数名 说明
np.sum() 求和
np.prod() 所有元素相乘
np.mean() 平均值
np.std() 标准差
np.var() 方差
np.median() 中位数
np.power() 幂运算
np.sqrt() 开方
np.min() 最小值
np.max() 最大值
np.argmin() 最小值的下标
np.argmax() 最大值的下标
np.inf 无穷大
np.exp(10) 以 e 为底的指数
np.log(10) 对数
'''
#以其中一个函数的使用为例 其他的函数的使用方法类似
import numpy as np
a = np.arange(12).reshape(3,4)
print(a)
a= np.power(a,2)
print(a)