# mro()函数用于打印类之间的继承结构

"""
Python 支持多重继承，一个子类可以继承多个父类。继承的语法格式如下：
        class 子类类名(父类 1[，父类 2，...])：
            类体
如果在类定义中没有指定父类，则默认父类是 object 类。也就是说，obje
ct 是所有类的父类，里面定义了一些所有类共有的默认实现，比如：__new_
_()。定义子类时，必须在其构造函数中调用父类的构造函数。调用格式如下
：父类名.__init__(self, 参数列表)<一般情况下子类需要调用父类构造
器>
"""


# 测试继承的基本使用

class Person:

    # 定义属性

    def __init__(self, name, age):
        self.name = name  # 共有属性
        self.__age = age  # 私有属性

    # 定义函数
    def say_age(self):
        print("age ? I don't know!")


class Student(Person):

    # 定义子类的构造器
    def __init__(self, name, age, score):
        # 首先调用父类的构造器<这样写可以提现继承的优势>
        Person.__init__(self, name, age)
        self.score = score


# Student->Person->object
# 使用mro()打印一个类的继承细节
print(Student.mro())  # 打印结果是从右向左的继承关系
