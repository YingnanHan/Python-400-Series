# coding:utf-8

# 新增功能：
#   1.设置我方坦克无限重生
#   2.按下ESC键使得坦克重生 重新创建我方坦克


# 导入pygame模块

import pygame
import random

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BG_COLOR = pygame.Color(0, 0, 0)  # 设置RGB颜色对象
TEXT_COLOR = pygame.Color(255, 0, 0)


#定义一个精灵类基类  用于后续的碰撞检测
class BaseItem(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)


class MainGame():
    # 用于保存窗口对象
    window = None
    my_tank = None

    # 存储敌方坦克的列表
    enemyTankList = []
    # 定义敌方坦克的数量
    enemyTankCount = 5
    #存储敌方子弹的列表
    enemyBulletList = []
    #存储爆炸效果的列表
    explodeList = []


    #存储我方子弹的列表
    myBulletList = []

    def __init__(self):
        pass

    # 开始游戏
    def startGame(self):
        # 加载主窗口  初始化窗口
        pygame.display.init()
        # 设置初始化窗口大小并且以屏幕进行显示并且得到返回的窗口surface对象
        MainGame.window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        # 初始化我方坦克
        self.createMyTank()
        # 初始化敌方坦克并将敌方坦克添加到列表中
        self.createEnemyTank()
        # 设置游戏窗口的标题
        pygame.display.set_caption("坦克大战1.03")
        # 使得游戏界面一直显示
        while True:
            # 使得坦克移动的速度移动的慢一些
            import time
            time.sleep(0.02)
            # 给窗口设置填充色为指定颜色
            MainGame.window.fill(color=BG_COLOR)
            # 获取事件
            self.getEvent()
            # 绘制文字 将文字surface绘制到另一个surface上面 也就是将子窗口放置在父窗口的指定位置
            MainGame.window.blit(self.getTextSurface("敌方坦克剩余数量%d" % len(MainGame.enemyTankList)), (10, 10))

            # 调用显示坦克的方法
            # 判断我方坦克是否存活
            if MainGame.my_tank and MainGame.my_tank.live:
                MainGame.my_tank.displayTank()
            else:
                #删除我方坦克
                del MainGame.my_tank
                MainGame.my_tank = None
            # 循环遍历敌方坦克列表，展示敌方坦克
            self.blitEnemyTank()
            # 循环遍历显示我方坦克子弹
            self.blitMyBullet()

            #循环遍历敌方子弹列表，展示敌方子弹
            self.blitEnemyBullet()
            #循环遍历爆炸列表展示爆炸效果
            self.blitExplode()

            # 调用移动坦克的方法
            # 如果坦克移动的开关开启则可以移动
            if MainGame.my_tank and MainGame.my_tank.live:
                if not MainGame.my_tank.stop:
                    MainGame.my_tank.move()
            # 刷新所做的修改
            pygame.display.update()


    #创建我方坦克的方法
    def createMyTank(self):
        MainGame.my_tank = Tank(350, 250)

    #循环展示爆炸效果
    def blitExplode(self):
        for explode in MainGame.explodeList:
            #判断是否活着
            if explode.live:
                #展示
                explode.displayExplode()
            else:
                #在爆炸列表中移除
                MainGame.explodeList.remove(explode)

    # 循环遍历敌方坦克列表，展示敌方坦克
    def blitEnemyTank(self):
        for enemyTank in MainGame.enemyTankList:
            #判断当前敌方坦克是否活着
            if enemyTank.live:
                enemyTank.displayTank()
                enemyTank.randMove()
                #设置敌方坦克发射子弹

                #创建子弹
                enemyBullet = enemyTank.shot()#这里的self是一个敌方坦克对象
                #判断生成的敌方子弹是否为空如果不是将其添加到列表
                if enemyBullet != None:
                    #将敌方子弹存储到敌方子弹列表
                    MainGame.enemyBulletList.append(enemyBullet)
            else:
                #将敌方坦克从敌方坦克列表中移除
                MainGame.enemyTankList.remove(enemyTank)


    # 显示我方发射的子弹
    def blitMyBullet(self):
        for myBullet in MainGame.myBulletList:
            #判断当前的子弹是否为live==True状态，如果是，则进行显示和移动，否则从列表中删除
            if myBullet.live:
                myBullet.displayBullet()
                #调用子弹移动方法
                myBullet.move()
                #调用函数检测我方坦克是否与敌方坦克发生碰撞
                myBullet.myBullet_hit_enemyTank()
            else:
                #删除对应的子弹
                MainGame.myBulletList.remove(myBullet)

    # 显示敌方发射的子弹
    def blitEnemyBullet(self):
        for enemyBullet in MainGame.enemyBulletList:
            # 判断当前的子弹是否为live==True状态，如果是，则进行显示和移动，否则从列表中删除
            if enemyBullet.live:#判断敌方子弹是否存活
                enemyBullet.displayBullet()
                enemyBullet.move()
                #调用敌方子弹与我方坦克碰撞的方法
                enemyBullet.enemyBullet_hit_myTank()
            else:
                MainGame.enemyBulletList.remove(enemyBullet)

    # 结束游戏
    def endGame(self):
        print("游戏结束，欢迎下次使用！·")
        exit()

    # 左上角文字的绘制  最终得到一个小的surface
    def getTextSurface(self, text):
        # 初始化字体模块
        pygame.font.init()
        # 查看所有的系统内置字体
        # print(pygame.font.get_fonts())
        # 获取字体font对象
        font = pygame.font.SysFont("华文楷体", 18)
        # 在新的surface上面绘制文本
        textSurface = font.render(text, True, TEXT_COLOR)
        return textSurface

    # 获取事件 相当于一个事件分发器
    def getEvent(self):
        # 获取所有的事件
        eventList = pygame.event.get()
        # 遍历事件列表
        for event in eventList:
            # 判断按下的键是关闭按钮还是普通键盘按钮

            # 如果按下的是退出按钮，关闭窗口
            if event.type == pygame.QUIT:
                self.endGame()

            # 如果按下的是普通的按钮
            if event.type == pygame.KEYDOWN:
                #当坦克不存在或者死亡按下ESC使得坦克重生
                if not MainGame.my_tank:
                    #判断按下的键是ESC，使得坦克重生
                    if event.key == pygame.K_ESCAPE:
                        #调用创建坦克的方法
                        self.createMyTank()
                        
                if MainGame.my_tank and MainGame.my_tank.live:
                    # 对于方向键的判断
                    if event.key == pygame.K_LEFT:  # ←键
                        # 首先切换坦克的方向
                        MainGame.my_tank.direction = 'L'
                        MainGame.my_tank.stop = False  # 使得坦克可以移动
                        # MainGame.my_tank.move()
                        print("按下←键，坦克向左移动")
                    elif event.key == pygame.K_RIGHT:  # →键
                        MainGame.my_tank.direction = 'R'
                        MainGame.my_tank.stop = False  # 使得坦克可以移动
                        # MainGame.my_tank.move()
                        print("按下→键，坦克向右移动")
                    elif event.key == pygame.K_UP:  # ↑键
                        MainGame.my_tank.direction = 'U'
                        MainGame.my_tank.stop = False  # 使得坦克可以移动
                        # MainGame.my_tank.move()
                        print("按下↑键，坦克向上移动")
                    elif event.key == pygame.K_DOWN:  # ↓键
                        MainGame.my_tank.direction = 'D'
                        MainGame.my_tank.stop = False  # 使得坦克可以移动
                        # MainGame.my_tank.move()
                        print("按下↓键，坦克向下移动")
                    elif event.key == pygame.K_SPACE:  # 如果按下空格键
                        #按下空格键以后，首先创建子弹 并且设置一次性最多可以创建三颗子弹
                        #如果当前我方当前子弹列表的大小 小于等于3的时候才可以创建
                        if len(MainGame.myBulletList)<3:
                            #创建我方坦克发射的子弹
                            myBulllet = Bullet(MainGame.my_tank)
                            #添加我方子弹到我方存储列表里面
                            MainGame.myBulletList.append(myBulllet)



            # 如果松开方向键，坦克停止移动 修改坦克的开关状态
            if event.type == pygame.KEYUP:
                # 判断松开的键是方向键吗？
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or \
                        event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    if MainGame.my_tank and MainGame.my_tank.live:
                        # 不按下按键的时候就停止移动
                        MainGame.my_tank.stop = True

    # 创建敌方坦克
    def createEnemyTank(self):
        top = 100
        # 循环生成敌方坦克
        for i in range(MainGame.enemyTankCount):
            left = random.randint(0, 600)
            speed = random.randint(1, 4)
            enemy = EnemyTank(left, top, speed)
            MainGame.enemyTankList.append(enemy)


class Tank(BaseItem):

    # 添加坦克距离左边的距离以及距离右边的距离
    def __init__(self, left, top):
        # 保存加载的图片
        self.images = {
            "U": pygame.image.load("img/p1tankU.gif"),
            "D": pygame.image.load("img/p1tankD.gif"),
            "L": pygame.image.load("img/p1tankL.gif"),
            "R": pygame.image.load("img/p1tankR.gif")
        }
        # 方向
        self.direction = "L"
        # 根据当前图片的方向获取图片surface
        self.image = self.images[self.direction]
        # 根据图片获取区域 默认情况下如果不指定，默认添加的内容是加载到左上角
        self.rect = self.image.get_rect()
        # 设置区域 left top值
        self.rect.left = left
        self.rect.top = top
        # 设置坦克移动的速度
        self.speed = 5
        # 设置弹可移动的开关
        self.stop = True  # 默认设置为停止
        #当前坦克是否活着的标记
        self.live = True

    # 移动
    def move(self):
        # 对坦克进行移动操作实际上就是设计坦克当前距离屏幕左上角的相对位置
        # 判断坦克的方向进行移动
        if self.direction == "L":
            if self.rect.left > 0:  # 限制向左移动不得超出屏幕范围
                self.rect.left -= self.speed
        elif self.direction == "U":
            if self.rect.top > 0:  # 限制向上移动不得超出屏幕范围
                self.rect.top -= self.speed
        elif self.direction == "D":
            if self.rect.top + self.rect.height < SCREEN_HEIGHT:  # 限制向下移动不得超出屏幕范围
                self.rect.top += self.speed
        elif self.direction == "R":
            if self.rect.left + self.rect.height < SCREEN_WIDTH:  # 限制向右移动不得超出屏幕范围
                self.rect.left += self.speed

    # 射击
    def shot(self):
        #返回子弹对象
        return Bullet(self)

    # 展示坦克
    def displayTank(self):
        # 获取展示的对象
        self.image = self.images[self.direction]
        # 调用blit函数展示对象  展示图片   展示图片位置
        MainGame.window.blit(self.image, self.rect)


# 我方坦克类
class MyTank(Tank):

    def __init__(self):
        pass


# 敌方坦克类
class EnemyTank(Tank):

    # 初始化敌方坦克的位置以及行驶速度
    def __init__(self, left, top, speed):
        #调用父类的初始化方法
        super(EnemyTank,self).__init__(left,top)
        # 加载图片集合
        self.images = {
            'U': pygame.image.load("img/enemy1U.gif"),
            'D': pygame.image.load("img/enemy1D.gif"),
            'L': pygame.image.load("img/enemy1L.gif"),
            'R': pygame.image.load("img/enemy1R.gif"),
        }
        # 设置可选择的方向 随机生成敌方坦克的方向
        self.direction = self.randDirection()
        # 根据所生成的方向，设置敌方坦克的图形
        self.image = self.images[self.direction]
        # 设置区域
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        # 设置初始速度
        self.speed = speed
        # 移动开关键
        self.flag = True
        # 步数
        self.step = 20

    # 随机生成坦克的方向
    def randDirection(self):
        num = random.randint(1, 4)
        if num == 1:
            return 'U'
        if num == 2:
            return 'D'
        if num == 3:
            return 'L'
        if num == 4:
            return 'R'

    # 敌方坦克随机移动的方法
    def randMove(self):
        if self.step < 0:
            # 修改方向
            self.direction = self.randDirection()
            # 让步数复位
            self.step = 60
        else:
            # 随机移动
            self.move()
            # 步数递减
            self.step -= 1


    #重写shot方法
    def shot(self):
        #随机生成100以内的数字
        import random
        num = random.randint(1,100)
        if num<10:
            #创建子弹
            return Bullet(self)


# 子弹类
class Bullet(BaseItem):

    def __init__(self, tank):
        # 加载图片
        self.image = pygame.image.load("img/enemymissile.gif")
        # 坦克的方向决定子弹发射的方向
        self.direction = tank.direction
        # 获取区域
        self.rect = self.image.get_rect()
        # 子弹的left与top和坦克的方向有关系
        if self.direction == 'U':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top - self.rect.height
        if self.direction == 'D':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height
        if self.direction == 'L':
            self.rect.left = tank.rect.left - self.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height / 2 - self.rect.width / 2
        if self.direction == 'R':
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top - self.rect.width / 2 + tank.rect.width / 2

        # 子弹的速度
        self.speed = 6
        #子弹的状态是否碰到墙壁，如果碰到墙壁，那么修改此状态
        self.live = True


    # 移动
    def move(self):
        if self.direction == "U":
            if self.rect.top>0:
                self.rect.top-=self.speed#向上移动
            else:
                #处理：当子弹撞墙时，修改其状态
                self.live = False

        if self.direction == "R":
            if self.rect.left+self.rect.width < SCREEN_WIDTH:
                self.rect.left += self.speed  # 向右移动
            else:
                # 处理：当子弹撞墙时，修改其状态
                self.live = False

        if self.direction == "L":
            if self.rect.left>0:
                self.rect.left-=self.speed  #向左移动
            else:
                # 处理：当子弹撞墙时，修改其状态
                self.live = False

        if self.direction == "D":
            if self.rect.top + self.rect.height < SCREEN_HEIGHT:
                self.rect.top += self.speed #向下移动
            else:
                # 处理：当子弹撞墙时，修改其状态
                self.live = False


    # 展示子弹的方法
    def displayBullet(self):
        # 将图片surface加载到窗口
        MainGame.window.blit(self.image, self.rect)


    #我方子弹与敌方坦克的碰撞
    def myBullet_hit_enemyTank(self):
        #循环遍历敌方坦克列表判断是否发生碰撞
        for enemyTank in MainGame.enemyTankList:
            if pygame.sprite.collide_rect(enemyTank,self):
                #如果敌方坦克与我方子弹发生碰撞，修改敌方坦克以及我方子弹的状态
                #是他们不再显示
                enemyTank.live = False
                self.live = False
                #创建爆炸对象将爆炸对象添加到爆炸列表中
                explode = Explode(enemyTank)
                MainGame.explodeList.append(explode)

    #敌方子弹与我方坦克的碰撞
    def enemyBullet_hit_myTank(self):
        #只有我方坦克存活的时候才进行检测否则会导致错误
        if MainGame.my_tank and MainGame.my_tank.live:
            if pygame.sprite.collide_rect(MainGame.my_tank,self):
                #产生爆炸对象
                explode = Explode(MainGame.my_tank)
                #将爆炸对象添加到爆炸列表中
                MainGame.explodeList.append(explode)
                #修改敌方子弹与我方坦克的状态
                self.live = False
                MainGame.my_tank.live = False


# 墙壁类
class Wall():

    def __init__(self):
        pass

    # 展示墙壁的方法
    def display(self):
        pass


# 爆炸效果类
class Explode():

    def __init__(self,tank):
        #爆炸的位置有当前子弹打中的坦克位置决定
        self.rect = tank.rect
        #存放爆炸效果图片
        self.images = [
            pygame.image.load("img/blast0.gif"),
            pygame.image.load("img/blast1.gif"),
            pygame.image.load("img/blast2.gif"),
            pygame.image.load("img/blast3.gif"),
            pygame.image.load("img/blast4.gif")
        ]

        self.step = 0
        self.image = self.images[self.step]
        #是否活着
        self.live=True


    # 展示爆炸效果
    def displayExplode(self):
        if self.step<len(self.images):
            #根据索引获取爆炸对象
            self.image = self.images[self.step]
            self.step+=1
            #添加到主窗口
            MainGame.window.blit(self.image,self.rect)
        else:
            #修改活着的状态
            self.live=False
            self.step=0


# 音效类
class Music():
    def __init__(self):
        pass

    # 播放音乐
    def play(self):
        pass


if __name__ == '__main__':
    # 定义一个窗口对象并且显示
    MainGame().startGame()

    # 查看系统内置字体
    # MainGame().getTextSurface()