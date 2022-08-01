# 运算符重载 以*的重载为例

class Person:

    def __init__(self, name):
        self.name = name

    def __mul__(self, other):
        if isinstance(other, int):
            return str(self.name) * other


p1 = Person("Mike")
print(p1 * 9)
