"""
Python支持多继承，如果多个父类具有同名的方法，在子类没有指定的时候，解释器将从左到右
按顺序搜索。
MRO指的是方法解析顺序，可以通过mro()方法获得类的层次结构，方法解析也是按照这个类的层
次结构寻找的，内层的解析策略是广度优先搜索
"""


# 测试mro的解析顺序
class A:
    def aa(self):
        print("aa")

    def say(self):
        print("say AAA!")


class B:
    def bb(self):
        print("bb")

    def say(self):
        print("say BBB!")


# 测试不同的继承循序带来的影响
class C(A, B):
    # class C(B,A):
    def cc(self):
        print("cc")


c = C()
c.cc()
c.bb()
c.aa()

# 打印类的层次结构
print(C.mro())
c.say()  # 解析器寻找say()方法侧顺序是从左到右，此时会执行B类中的say()方法
