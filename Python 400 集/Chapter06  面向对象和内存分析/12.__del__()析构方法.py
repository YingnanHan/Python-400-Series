'''
__del__()方法称为析构方法，用于实现对象被销毁所需要的操作，比如：释放对象占用的资源（例如
打开文件的资源，网络连接等）
Python实现自动的垃圾回收机制，当对象没有被引用时（引用计数为0），有垃圾回收机器调用del放法
我们也可以使用del语句删除对象，从而保证调用__del__放法。系统会自动调用__del__()，一般不需
要自定义析构方法。
'''


# 测试析构函数
class Person:

    def __init__(self):
        print("销毁对象：{0}".format(self))

    def __del__(self):
        print("析构函数被调用")


p1 = Person()
p2 = Person()
del p2
print("程序结束")
print(p1)
# print(p2)#p2已经被手动销毁了不可调用
