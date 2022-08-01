# 测试has-a关系，使用组合

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


# 使用组合
m = MobilePhone(CPU(), Screen())
m.cpu.calculate()
m.screen.show()
