"""
1.成员继承：子类继承了父类除构造方法之外的全部成员
2.方法重写：子类可以重新定义父类中的方法，这样就会覆盖父类方法，也成为重写
"""


# 例子

class Person:

    def __init__(self, name, age):
        self.name = name  # 共有属性
        self.__age = age  # 私有属性

    def say_age(self):
        print("我的年龄：", self.__age)

    def say_introduce(self):
        print("我的名字是{0}".format(self.name))


class Student(Person):

    def __init__(self, name, age, score):
        Person.__init__(self, name, age)  # 必须显示的调用父类的初始化方法，不然解释器不会去调用
        self.score = score

    # 重写父类的方法
    def say_introduce(self):
        print("Sir！！ My name is {0}".format(self.name))


s = Student("Mike", 18, 80)
s.say_age()
s.say_introduce()  # 一旦子类重写父类的方法之后如果不加以限制，那么优先调用的就是子类的方法
