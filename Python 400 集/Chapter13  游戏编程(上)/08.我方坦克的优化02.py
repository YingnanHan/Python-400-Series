# coding:utf-8

#新增功能：
#   1.按下方向键坦克一直移动
#   2.松开方向键坦克停止移动


#导入pygame模块
import pygame

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BG_COLOR = pygame.Color(0,0,0)#设置RGB颜色对象
TEXT_COLOR = pygame.Color(255,0,0)


class MainGame():

    #用于保存窗口对象
    window = None
    my_tank = None

    def __init__(self):
        pass

    # 开始游戏
    def startGame(self):
        #加载主窗口  初始化窗口
        pygame.display.init()
        #设置初始化窗口大小并且以屏幕进行显示并且得到返回的窗口surface对象
        MainGame.window = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
        #初始化我方坦克
        MainGame.my_tank = Tank(350,250)
        # 设置游戏窗口的标题
        pygame.display.set_caption("坦克大战1.03")
        #使得游戏界面一直显示
        while True:
            #使得坦克移动的速度移动的慢一些
            import time
            time.sleep(0.02)
            #给窗口设置填充色为指定颜色
            MainGame.window.fill(color=BG_COLOR)
            #获取事件
            self.getEvent()
            #绘制文字 将文字surface绘制到另一个surface上面 也就是将子窗口放置在父窗口的指定位置
            MainGame.window.blit(self.getTextSurface("敌方坦克剩余数量%d"%6),(10,10))
            #调用显示坦克的方法
            MainGame.my_tank.displayTank()
            #调用移动坦克的方法
            #如果坦克移动的开关开启则可以移动
            if not MainGame.my_tank.stop:
                MainGame.my_tank.move()
            #刷新所做的修改
            pygame.display.update()


    # 结束游戏
    def endGame(self):
        print("游戏结束，欢迎下次使用！·")
        exit()


    #左上角文字的绘制  最终得到一个小的surface
    def getTextSurface(self,text):
        #初始化字体模块
        pygame.font.init()
        #查看所有的系统内置字体
        #print(pygame.font.get_fonts())
        #获取字体font对象
        font = pygame.font.SysFont("华文楷体",18)
        #在新的surface上面绘制文本
        textSurface = font.render(text,True,TEXT_COLOR)
        return textSurface


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
                    #首先切换坦克的方向
                    MainGame.my_tank.direction = 'L'
                    MainGame.my_tank.stop = False#使得坦克可以移动
                    #MainGame.my_tank.move()
                    print("按下←键，坦克向左移动")
                elif event.key == pygame.K_RIGHT:#→键
                    MainGame.my_tank.direction = 'R'
                    MainGame.my_tank.stop = False#使得坦克可以移动
                    #MainGame.my_tank.move()
                    print("按下→键，坦克向右移动")
                elif event.key == pygame.K_UP:#↑键
                    MainGame.my_tank.direction = 'U'
                    MainGame.my_tank.stop = False  # 使得坦克可以移动
                    #MainGame.my_tank.move()
                    print("按下↑键，坦克向上移动")
                elif event.key == pygame.K_DOWN:#↓键
                    MainGame.my_tank.direction = 'D'
                    MainGame.my_tank.stop = False  # 使得坦克可以移动
                    #MainGame.my_tank.move()
                    print("按下↓键，坦克向下移动")
                elif event.key == pygame.K_SPACE:#如果按下空格键
                    print("发射子弹")

            #如果松开方向键，坦克停止移动 修改坦克的开关状态
            if event.type == pygame.KEYUP:
                # 判断松开的键是方向键吗？
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or\
                    event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    # 不按下按键的时候就停止移动
                    MainGame.my_tank.stop = True

class Tank():

    #添加坦克距离左边的距离以及距离右边的距离
    def __init__(self,left,top):
        #保存加载的图片
        self.images={
            "U":pygame.image.load("img/p1tankU.gif"),
            "D":pygame.image.load("img/p1tankD.gif"),
            "L":pygame.image.load("img/p1tankL.gif"),
            "R":pygame.image.load("img/p1tankR.gif")
        }
        #方向
        self.direction = "L"
        #根据当前图片的方向获取图片surface
        self.image = self.images[self.direction]
        #根据图片获取区域 默认情况下如果不指定，默认添加的内容是加载到左上角
        self.rect = self.image.get_rect()
        #设置区域 left top值
        self.rect.left = left
        self.rect.top = top
        #设置坦克移动的速度
        self.speed = 5
        #设置弹可移动的开关
        self.stop = True#默认设置为停止

    # 移动
    def move(self):
        #对坦克进行移动操作实际上就是设计坦克当前距离屏幕左上角的相对位置
        #判断坦克的方向进行移动
        if self.direction == "L":
            if self.rect.left >0:#限制向左移动不得超出屏幕范围
                self.rect.left -= self.speed
        elif self.direction == "U":
            if self.rect.top >0:#限制向上移动不得超出屏幕范围
                self.rect.top -= self.speed
        elif self.direction == "D":
            if self.rect.top+self.rect.height<SCREEN_HEIGHT:#限制向下移动不得超出屏幕范围
                self.rect.top += self.speed
        elif self.direction == "R":
            if self.rect.left+self.rect.height<SCREEN_WIDTH:#限制向右移动不得超出屏幕范围
                self.rect.left += self.speed
    # 射击
    def shot(self):
        pass

    # 展示坦克
    def displayTank(self):
        #获取展示的对象
        self.image = self.images[self.direction]
        #调用blit函数展示对象  展示图片   展示图片位置
        MainGame.window.blit(self.image,self.rect)

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

    #查看系统内置字体
    #MainGame().getTextSurface()