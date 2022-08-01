# 测试类对象的生成
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def say_score(self):
        print("{0}的分数是，{1}".format(self.name, self.score))


"""
可以看到实际上生成了一个变量名，就是Student的对象，可以通过复制操作将其赋值给Stu，这样也可以实现
相关的调用，说明确实可以创建类对象，也就是说Stu是对Student类对象的一个引用
"""

print(type(Student))
print(id(Student))

Stu = Student  # 引用
s1 = Stu()  # 定义一个类对象
print(s1)
print(Student)
