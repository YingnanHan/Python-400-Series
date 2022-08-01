# 测试重写object的__str__()方法

class Person:  # 默认继承object类

    def __init__(self, name):
        self.name = name

    # 重写__str__()方法
    def __str__(self):
        return "名字是{0}".format(self.name)


p = Person("Mike")
print(p)  # 注意当一个对象被定义并且被输出的时候，实际上输出的内容是被__str__()内置方法所控制
