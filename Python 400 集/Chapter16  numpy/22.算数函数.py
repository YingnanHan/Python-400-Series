'''
如果参与运算的两个对象，都是ndarray并且形状相同，那么就会对两个矩阵的对应位置之间进行四则运算
numpy中包含的算术运算有：add()  subtract()  multiply()  divide()
'''
import numpy as np

a = np.arange(9,dtype=np.float).reshape(3,3)
b = np.array([10,10,10])
print("第一个数组\n",a)
print("第二个数组\n",b)

#进行四则运算
print(np.add(a,b))#将b加到a的每一行
print(np.subtract(a,b))#将b减去a的每一行
print(np.multiply(a,b))#将b乘以a的每一行
print(np.divide(a,b))#将b除以a的每一行

print("*-------------------*")
#out参数的使用
y = np.empty(9).reshape(3,3)#创建一个3X3的数组
print(y)
np.multiply(a,10,out=y)#之句话的意思是将执行结束的乘法操作的结果输出到y矩阵中
print("the result is；")
print(y)