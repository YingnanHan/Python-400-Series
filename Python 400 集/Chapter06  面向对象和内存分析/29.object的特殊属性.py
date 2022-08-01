# 测试特殊属性
'''
特殊方法 含义
obj.__dict__            对象的属性字典
obj.__class__           对象所属的类
class.__bases__         类的基类元组（多继承）
class.__base__          类的基类
class.__mro__           类层次结构
class.__subclasses__()  子类列表
'''


class A:
    pass


class B:
    pass


class C(B, A):

    def __init__(self, nn):
        self.nn = nn

    def cc(self):
        print("cc")


c = C(3)
print(dir(c))
print(c.__dict__)
print(c.__class__)
print(C.__bases__)
print(C.mro())
print(A.__subclasses__())
