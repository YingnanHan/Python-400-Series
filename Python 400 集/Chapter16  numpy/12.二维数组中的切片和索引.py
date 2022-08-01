#导入numpy模块
import numpy as np
#创建一维数组
a = np.arange(1,13)
print(a)
#reshape 对一维数组进行修改维数 并且改变形状
a = a.reshape([4,3])  #值得注意的是 reshape里面的维数参数可以是元组或者列表
print(a)

#二维数组索引的使用
#获取第三行
print(a[2])
#获取第二行第三列
print(a[1][2])

#二维数组切片的使用  [<对行进行切片>start:stop:step,<对列进行切片>start:stop:step]
#1.获取所有行 以及所有列 [][]
print(a[:,:])
#2.获取所有行第二列  得到的结果是一个一维数组
print(a[:,1])
#3.获取所有行的部分列
print(a[:,0:2])
#4.获取所有列的部分行
print(a[0:5:2,:])#获取奇数行所有列
#5.获取部分行部分列
print(a[0:5:2,[1,2]]) #具体的列号可以使用列表给出


#使用坐标获取数组中的数据
print(a[2,1])#得到第二行第一列的数据
print(a[2][1])#效果同上

#同时获取不同行不同列
print(a[2,1],a[2,0])
#将获取的数据合并为一个数组
print(np.array([a[2,1],a[2,0]]))
#使用坐标来合并数组
print(a[(1,2),(1,2)])#这句话的意思是前面的元组中的元素作为坐标，后面的座位y的坐标，然后对应位置作拼接


#负数索引的使用

print("二维数组的最后一行",a[-1])
print("行的倒序\n",a[::-1])
print("行与列的倒序\n",a[::-1,::-1])#这句话的意思是先对行进行倒序，然后对列进行倒序