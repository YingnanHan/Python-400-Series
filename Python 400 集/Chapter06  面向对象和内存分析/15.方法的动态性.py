# 测试方法的动态性

class Person:

    def work(self):
        print("努力上班！！！")


def play_game(name):  # 这里必须要有一个参数和类内部函数的self是对应的
    print("{0}在玩游戏".format(name))


def work2(name):  # 这里必须要有一个参数和类内部函数的self是对应的
    print("上班摸鱼！！！")


# 为类添加新的的函数
Person.play_game = play_game
p = Person()
p.work()
p.play_game()  # Person的对象可以直接调用Person类新添加的函数  其本质是Person.play_game(p)

# 修改类内部函数
Person.work = work2
p.work()
