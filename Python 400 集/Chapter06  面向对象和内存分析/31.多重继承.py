# 多重继承实例

class A:
    def aa(self):
        print("aa")


class B:
    def bb(self):
        print("bb")


class C(B, A):
    def cc(self):
        print("cc")


# 使用多重继承之后，最低级的继承者可以使用其祖先各个类的所有的公开的方法
c = C()
c.cc()
c.bb()
c.aa()
