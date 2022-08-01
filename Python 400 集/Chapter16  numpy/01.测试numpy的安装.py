import numpy as np

#使用numpy生成一个数组
array = np.arange(10)
print(array)
print(type(array))


#对列表中的元素开平方

#传统方法
import math
b = [3,4,9]
#定义存储开平方结果的列表   2qtb
res = []
#遍历列表
for i in b:
    print(math.sqrt(i))
    res.append(math.sqrt(i))
print(res)

#numpy方法
#对ndarray对象直接作为一个向量进行处理,这样会提高实际的运算效率
print(np.sqrt(b))