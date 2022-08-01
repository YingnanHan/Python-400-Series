class Student:  # 类名一般首字母大写，多个单词采用驼峰原则
    # 构造方法
    def __init__(self, name, score):  # self必须位于第一个参数
        self.name = name
        self.score = score

    def say_score(self):  # self必须位于第一个参数
        print("{0}的分数是，{1}".format(self.name, self.score))


# 不同的实例在一定条件下可能有不同的属性


# 定义类对象
s1 = Student("Mike", 18)
s1.say_score()
# 可以对已经定义的对象新增加属性
s1.age = 32
s1.salary = 3000
# 但是如果另外定义一个对象，刚才仅仅针对s1添加的属性就不会出现在新对象之中
s2 = Student("John", 12)
print(s2.name)
