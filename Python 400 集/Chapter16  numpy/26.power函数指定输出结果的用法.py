import numpy as np

x = np.arange(5)
y = np.zeros(10)

np.power(2,x,out=y[:5])#将x中的每一个元素都进行2^x次方操作，然后重定向输出到y的前五个元素之中
print("power",x)
print(y)