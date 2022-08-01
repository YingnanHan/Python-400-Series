# coding:utf-8

#新增功能：事件处理
#   1.点击关闭 关闭窗口
#   2.按下键盘之后如果判断键盘按下的是某一个确定的按键，分别对不同的Key做处理
#   pygame官方网址：www.pygame.org

#导入pygame模块
import pygame

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BG_COLOR = pygame.Color(0,0,0)#设置RGB颜色对象

class MainGame():

    #用于保存窗口对象
    window = None

    def __init__(self):
        pass

    # 开始游戏
    def startGame(self):
        #加载主窗口  初始化窗口
        pygame.display.init()
        #设置初始化窗口大小并且以屏幕进行显示并且得到返回的窗口surface对象
        MainGame.window = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
        #设置游戏窗口的标题
        pygame.display.set_caption("坦克大战1.03")
        #使得游戏界面一直显示
        while True:
            #给窗口设置填充色为指定颜色
            MainGame.window.fill(color=BG_COLOR)
            #获取事件
            self.getEvent()

            pygame.display.update()

        pass

    # 结束游戏
    def endGame(self):
        print("游戏结束，欢迎下次使用！·")
        exit()


    #获取事件 相当于一个事件分发器
    def getEvent(self):
        #获取所有的事件
        eventList = pygame.event.get()
        #遍历事件列表
        for event in eventList:
            #判断按下的键是关闭按钮还是普通键盘按钮

            #如果按下的是退出按钮，关闭窗口
            if event.type == pygame.QUIT:
                self.endGame()

            #如果按下的是普通的按钮
            if event.type == pygame.KEYDOWN:
                #对于方向键的判断
                if event.key == pygame.K_LEFT:#←键
                    print("按下←键，坦克向左移动")
                elif event.key == pygame.K_RIGHT:#→键
                    print("按下→键，坦克向右移动")
                elif event.key == pygame.K_UP:#↑键
                    print("按下↑键，坦克向上移动")
                elif event.key == pygame.K_DOWN:#↓键
                    print("按下↓键，坦克向下移动")

class Tank():

    def __init__(self):
        pass

    # 移动
    def move(self):
        pass

    # 射击
    def shot(self):
        pass

    # 展示坦克
    def display(self):
        pass


# 我方坦克
class MyTank(Tank):

    def __init__(self):
        pass


# 敌方坦克
class EnemyTank(Tank):

    def __init__(self):
        pass


# 子弹类
class Bullet():

    def __init__(self):
        pass

    # 移动
    def move(self):
        pass

    # 展示子弹的方法
    def displayBullet(self):
        pass


# 墙壁类
class Wall():

    def __init__(self):
        pass

    # 展示墙壁的方法
    def display(self):
        pass


# 爆炸效果类
class Explode():

    def __init__(self):
        pass

    # 展示爆炸效果
    def displayExplode(self):
        pass


# 音效类
class Music():
    def __init__(self):
        pass

    # 播放音乐
    def play(self):
        pass




if __name__ == '__main__':
    #定义一个窗口对象并且显示
    MainGame().startGame()