# 用来判断某一个对象是不是某一个类的实例对象
# 该内置函数可以获得对象的所有的属性和方法字典
class Student:  # 类名一般首字母大写，多个单词采用驼峰原则
    # 构造方法
    def __init__(self, name, score):  # self必须位于第一个参数
        self.name = name
        self.score = score

    def say_score(self):  # self必须位于第一个参数
        print("{0}的分数是，{1}".format(self.name, self.score))


class Max:
    pass  # 这里使用了pass占位，不会报错


s = Student("Mike", 19)
print(isinstance(s, Student))
print(isinstance(s, Max))
