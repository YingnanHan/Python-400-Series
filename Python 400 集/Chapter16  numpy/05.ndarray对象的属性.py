#导入numpy
import numpy as np

#创建一位数组
a = np.array([1,2,3,4])
print(a)
#创建二维数组
b = np.arange(4,10)
print(b)

b = np.random.randint(4,10,size=(2,3))#直接创建二维数组
print(b)

#创建三维数组
c = np.random.randn(2,3,4)#创建一个服从标准正太分布的三维数组
print(c)

#数组的属性参数

# ndim 获取数组的维数
print("ndim",a.ndim,b.ndim,c.ndim)
# shape 获取数组的规模
print("shape",a.shape,b.shape,c.shape)
# dtype 获取数组的类型
print("dtype",a.dtype,b.dtype,c.dtype)
# size  获取元素的总数目
print("size",a.size,b.size,c.size)
# itemsize  获取每一个元素所占据的字节数
print("itemsize",a.itemsize,b.itemsize,c.itemsize)

