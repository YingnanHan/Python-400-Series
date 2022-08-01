# 测试对象的浅拷贝

import copy


class MobilePhone:
    def __init__(self, cpu, screen):
        self.cpu = cpu
        self.screen = screen


class CPU:
    def calculate(self):
        print("calculating....")


class Screen:
    def show(self):
        print("showing....")


# 测试变量赋值
c1 = CPU()
c2 = c1
print(c1)  # 对CPU对象的引用
print(c2)  # 对m1的引用

# 测试浅拷贝
s1 = Screen()
c1 = CPU()
m1 = MobilePhone(c1, s1)
# 使用copy模块浅复制m1
m2 = copy.copy(m1)
# 子对象不会拷贝
print(m1, m1.cpu, m1.screen)
print(m2, m2.cpu, m2.screen)

# 测试深复制
s1 = Screen()
c1 = CPU()
m1 = MobilePhone(c1, s1)
# 使用copy模块浅复制m1
m2 = copy.deepcopy(m1)
# 子对象一同拷贝
print(m1, m1.cpu, m1.screen)
print(m2, m2.cpu, m2.screen)
