class Student:  # 类名一般首字母大写，多个单词采用驼峰原则
    # 构造方法
    def __init__(self, name, score):  # self必须位于第一个参数
        self.name = name
        self.score = score

    def say_score(self):  # self必须位于第一个参数
        print("{0}的分数是，{1}".format(self.name, self.score))


# 定义类对象
s1 = Student("Mike", 18)
s1.say_score()  # 当执行这句话的时候，解释器实际上执行的是Student.say_score(s1)
Student.say_score(s1)  # 也就是将s1.say_score()翻译为Student.say_score(s1)
# 类实际上是一个模具，方法是一种行为，是可以被所有对象共享的
