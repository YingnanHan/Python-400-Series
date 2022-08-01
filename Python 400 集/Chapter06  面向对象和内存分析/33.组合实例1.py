"""
组合用于处理如下类似问题
“is-a”关系，我们可以使用“继承”。从而实现子类拥有的父类的方法和属性。“is-a”
关系指的是类似这样的关系：狗是动物，dog is animal。狗类就应该继承动物类。
“has-a”关系，我们可以使用“组合”，也能实现一个类拥有另一个类的方法和属性。”
has-a”关系指的是这样的关系：手机拥有 CPU。 MobilePhone has a CPU。
"""


# 使用继承实现代码复用
class A1:

    def say_A1(self):
        print("a1")


class B1(A1):
    pass


b1 = B1()
b1.say_A1()


# 使用组合
class A2:

    def say_A2(self):
        print("a2")


class B2:
    # 不用继承使用A2方法的方法----将A2的对象作为自己的属性
    def __init__(self, A):
        self.A = A


a2 = A2()
b2 = B2(a2)
b2.A.say_A2()
# 简而言之就是b2对象在初始化的时候，参数包含一个A对象，b2通过使用自己的属性a2来间接调用
# A中的内容，进而实现了代码的复用
