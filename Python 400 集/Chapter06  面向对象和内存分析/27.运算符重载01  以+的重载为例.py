# 运算符重载

class Person:

    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Person):
            return "{0}--{1}".format(self.name, other.name)
        else:
            print("不是同类对象，禁止相加")


p1 = Person("Mike")
p2 = Person("John")
print(p1 + p2)
