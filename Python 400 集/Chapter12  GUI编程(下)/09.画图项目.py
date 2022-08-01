# coding:utf-8

from tkinter import *
from tkinter.dialog import *
from tkinter.colorchooser import *
from tkinter.messagebox import *
from tkinter.filedialog import *


win_width = 900                                         #设置窗口的宽度
win_height = 450                                        #设置窗口的高度

class Application(Frame):

    def __init__(self,master=None,bgcolor = "#000000"):

        super().__init__(master = master)               #初始化父类构造方法
        self.master = master                            #初始化master
        self.bgcolor = bgcolor                          #设置背景颜色
        self.x = 0                                      #设置当前位置的x坐标
        self.y = 0                                      #设置当前位置的y坐标
        self.lastDraw = 0                               #表示最后所绘制图形的id
        self.fgcolor = "#ff0000"                        #设置前景色，也就是画笔的颜色
        self.startDrawFlag = False                      #
        self.createWidgets()                            #在root上创建widgets
        self.pack()                                     #将创建的widgets放置在root上


    def createWidgets(self):
        # 创建绘图区
        self.drawpad = Canvas(self.master,width=win_width,height=win_height*0.9,bg=self.bgcolor)
        self.drawpad.pack()

        #创建按钮
        self.btn_start = Button(self.master,text="开始",name = "start")
        self.btn_start.pack(side="left",padx="10")

        self.btn_pen = Button(self.master, text="画笔", name="pen")
        self.btn_pen.pack(side="left", padx="10")

        self.btn_rect = Button(self.master, text="矩形", name="rect")
        self.btn_rect.pack(side="left", padx="10")

        self.btn_clear = Button(self.master, text="清屏", name="clear")
        self.btn_clear.pack(side="left", padx="10")

        self.btn_eraser = Button(self.master, text="橡皮擦", name="eraser")
        self.btn_eraser.pack(side="left", padx="10")

        self.btn_line = Button(self.master, text="直线", name="line")
        self.btn_line.pack(side="left", padx="10")

        self.btn_lineArrow = Button(self.master, text="箭头直线", name="lineArrow")
        self.btn_lineArrow.pack(side="left", padx="10")

        self.btn_color = Button(self.master, text="颜色", name="color")
        self.btn_color.pack(side="left", padx="10")

        #为按钮绑定事件
        self.btn_pen.bind_class("Button","<1>",self.eventManager)                   #按下左键的时候开始绘制
        self.drawpad.bind("<ButtonRelease-1>",self.stopDraw)                        #设置释放鼠标左键时停止绘画


        #增加颜色切换的快捷键
        self.master.bind("<KeyPress-r>",self.quickKeys)
        self.master.bind("<KeyPress-g>", self.quickKeys)
        self.master.bind("<KeyPress-b>", self.quickKeys)

    #事件管理器
    def eventManager(self,event):
        #用来获取当前事件的名称
        self.name = event.widget.winfo_name()

        if self.name == "line":
            self.drawpad.bind("<B1-Motion>",self.myline)
        if self.name == "lineArrow":
            self.drawpad.bind("<B1-Motion>", self.mylineArrow)
        if self.name == "rect":
            self.drawpad.bind("<B1-Motion>",self.myRect)
        if self.name == "pen":
            self.drawpad.bind("<B1-Motion>",self.myPen)
        if self.name == "eraser":
            self.drawpad.bind("<B1-Motion>",self.myEraser)
        if self.name == "clear":
            #将绘画板中的所有内容清楚
            self.drawpad.delete("all")
        if self.name == "color":
            #得到一个颜色选择框
            self.c = askcolor(color=self.fgcolor,title="选择画笔颜色")
            #修改前景色为所选择的颜色
            self.fgcolor = self.c[1]

    #开始绘制（绘制图形前的准备工作）
    def startDraw(self,event):
        # 将上一次所绘制直线的id删除，仅仅保留当前的直线的id
        self.drawpad.delete(self.lastDraw)
        # 保证初始位置是鼠标最开始点击的位置，并且不会被修改
        if not self.startDrawFlag:
            self.startDrawFlag = TRUE
            self.x = event.x
            self.y = event.y

    #停止绘制
    def stopDraw(self,event):
        #修改画图的时候的判定条件使得下一次绘制图形的时候可以启动一个新的直线
        self.startDrawFlag = False
        #为了使得上一次所绘制的图形不会因为myline函数的判断消失，设置上一次的直线的id为负数,系统默认的id为正整数
        self.lastDraw = 0

    #绘制直线
    def myline(self,event):

        self.startDraw(event)
        #获取最后所绘制直线的id
        self.lastDraw = self.drawpad.create_line(self.x,self.y,event.x,event.y,fill=self.fgcolor)

    # 绘制箭头
    def mylineArrow(self, event):

        self.startDraw(event)
        # 获取最后所绘制直线的id
        self.lastDraw = self.drawpad.create_line(self.x, self.y, event.x, event.y,arrow=LAST, fill=self.fgcolor)

    #绘制矩形
    def myRect(self,event):

        self.startDraw(event)
        #获取最后所绘制直线的id                                outline属性设置了绘制的图形是一个指定形状的边框
        self.lastDraw = self.drawpad.create_rectangle(self.x,self.y,event.x,event.y,outline=self.fgcolor)

    #绘制自定义曲线
    def myPen(self,event):
        self.startDraw(event)
        # 获取最后所绘制直线的id  这里由于是使用直线逼近曲线所以前一段的微小直线不需要删除
        # 也即下面这句话不需要赋值给self.lastDraw删除上一次绘制的结果
        self.drawpad.create_line(self.x, self.y, event.x, event.y, fill=self.fgcolor)
        self.x = event.x
        self.y = event.y

    #自定义橡皮擦
    def myEraser(self,event):
        #橡皮擦的实质就是将橡皮擦所走过的区域按照当前背景色填充
        self.startDraw(event)
        # 获取最后所绘制直线的id                                outline属性设置了绘制的图形是一个指定形状的边框
        self.lastDraw = self.drawpad.create_rectangle(event.x-4, event.y-4, event.x+4, event.y+4, fill=self.bgcolor)
        self.x = event.x
        self.y = event.y

    #自定义快捷键
    def quickKeys(self,event):
        if event.char == "r":
            self.fgcolor = "#ff0000"
        if event.char == "g":
            self.fgcolor = "#00ff00"
        if event.char == "b":
            self.fgcolor = "purple"

#主方法
if __name__ == '__main__':

    root = Tk()
    root.geometry(str(win_width)+"x"+str(win_height)+"+200+300")
    root.title("画图软件")
    app = Application(root)
    root.mainloop()