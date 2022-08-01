# 该内置函数可以获得对象的所有的属性和方法字典
class Student:  # 类名一般首字母大写，多个单词采用驼峰原则
    # 构造方法
    def __init__(self, name, score):  # self必须位于第一个参数
        self.name = name
        self.score = score

    def say_score(self):  # self必须位于第一个参数
        print("{0}的分数是，{1}".format(self.name, self.score))


s = Student("MIke", 15)
print(s.__dir__())
