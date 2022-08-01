# dir()函数用于查看一个类的所有属性 注意体会两个输出的区别

class Person:
    def __init__(self, name, age):
        self.name = name

        self.age = age

    def say_age(self):
        print(self.name, "的年龄是：", self.age)


obj = object()  # object是所有类的父类
print(dir(obj))
s2 = Person("高淇", 18)
print(dir(s2))
