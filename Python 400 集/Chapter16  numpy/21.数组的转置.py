#导入numpy模块
import numpy as np
#创建二维数组
arr = np.arange(1,25).reshape(8,3)
print(arr)
print("tranpose函数进行数组转置 \n",arr.transpose())

#值得注意的是对于二维数组可以使用.T函数来实现数组的转置
print("T进行数组转置 \n",arr.T)

#numpy中的transpose函数
print("使用numpy直接进行转置\n",np.transpose(arr))

#对多维数组进行转置
#多维数组转置的实质就是人为的对数组的维度坐标进行交换
print("对多维数组进行转置")
arr = arr.reshape(2,3,4)
print(arr,arr.shape)
print("对三维数组a[i][j][k]进行指定维度的转置")
c = np.transpose(arr,(1,2,0))
print(c)
print(c.shape)