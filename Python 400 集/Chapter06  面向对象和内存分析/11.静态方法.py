'''
“静态方法”和在模块中定义普通函数没有区别，只不过“静态方法”放到了“类的名字空
间里面”，需要通过“类调用”。
静态方法通过装饰器@staticmethod 来定义，格式如下：
@staticmethod
def 静态方法名([形参列表]) ：
函数体
要点如下：
1. @staticmethod 必须位于方法上面一行
2. 调用静态方法格式：“类名.静态方法名(参数列表)”。
3. 静态方法中访问实例属性和实例方法会导致错误
'''


class Student:
    company = "SXT"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def printCompany(cls):
        print(cls.company)
        # print(self.name)#类方法和静态方法中不能调用实例变量，实例方法

    @staticmethod  # 定义静态方法
    def add(a, b):  # 实际上静态方法和类方法之间的界线并不是那么清晰
        print("{0}+{1}={2}".format(a, b, a + b))
        return a + b


Student.add(1, 2)
