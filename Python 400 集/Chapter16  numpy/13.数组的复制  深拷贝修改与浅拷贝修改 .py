#导入numpy模块
import numpy as np
#创建一个二维数组
a = np.arange(1,13)
#创建一个二维数组
a = a.reshape([3,4])
print(a)
#对数组a进行一个切片  获取第1,2行 第 1,2列
sub_a = a[:2,:2]
print(sub_a)

#######浅拷贝修改
#对sub_a中的第一行第一列的值进行修改
sub_a[0][0] = 100
print(sub_a)
print(a)
#值得注意的是原来的数组也被修改 实际上通过果切片获
#得的新数组实际上是一个浅拷贝 对新数组的修改会导致
#原来的数的修改

########深拷贝修改
#使用numpy下的copy方法先深拷贝在修改
sub_b = np.copy(a[::2,::2])
print(sub_b)
sub_b[1][1] = 200#对元素进行修改，不会影响原来数组的值
print(sub_b)