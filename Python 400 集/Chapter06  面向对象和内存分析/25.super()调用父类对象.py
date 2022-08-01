# 测试super（）,代表父类的定义，而不是父类的对象

class A:

    def say(self):
        print("A", self)


class B(A):

    def say(self):
        # 使用父类的同名方法①
        # A.say(self)

        # 使用父类的同名方法②
        super(B, self).say()

        print("B", self)


B().say()
