"""
类属性是从属于类对象的属性，也称为类变量，由于类属性从属于类对象，可以被所有实例
对象共享

类属性定义方式：
    class <Name>:
        类变量名=初始值
在类中或者类的外面，可以通过：“类名.类变量名”来读写
"""


class Student:
    company = "SXT"  # 类属性
    count = 0  # 类属性

    def __init__(self, name, score):
        self.name = name  # 实例属性
        self.score = score  # 实例属性
        Student.count = Student.count + 1  # 在这里直接调用类属性，用来计算生成了对少对象

    def sayScore(self):
        # 通过类名调用类属性
        print("我的公司是{0}，综合得分是{1}".format(Student.company, self.score))


s1 = Student("张三", 80)  # s1是实例对象，自动调用__init__()方法
s1.sayScore()
print("一共创建了{0}个对象".format(Student.count))
