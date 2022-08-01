# coding:utf-8

from tkinter import *
from tkinter import messagebox
import random


class Application(Frame):

    def __init__(self, master):
        super().__init__(master=master)
        self.master = master
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # 定义一个画布对象设置它的长和宽以及背景颜色为绿色
        self.canvas = Canvas(width=300, height=200, bg="green")
        # 将画布pack到root上
        self.canvas.pack()
        # 画一条直线 参数指的是 起始点坐标(10,10) 中间点坐标(30,20) 中点坐标(40,50)
        line = self.canvas.create_line(10, 10, 30, 20, 40, 50)  # 这里的参数可以不限制传递，但是必须成对构成一个pair
        # 画一个矩形
        rect = self.canvas.create_rectangle(50, 50, 100, 100)
        # 画一个椭圆 参数指的是椭圆的矩形边界的
        oval = self.canvas.create_oval(50, 50, 100, 100)
        # 在一个确定的位置绘制图像
        global photo
        photo = PhotoImage(file=r"../Chapter10  GUI编程(上)/image/logo.gif")
        self.canvas.create_image(150, 170, image=photo)

        # 制做一个按钮 触发事件draw50Rect
        btn = Button(self, text="绘制10个矩形", command=self.draw50Rect)
        btn.pack(side="left")

    # 绘制10个矩形的函数
    def draw50Rect(self):
        for i in range(0, 10):
            x1 = random.randrange(int(self.canvas["width"]) / 2)
            y1 = random.randrange(int(self.canvas["height"]) / 2)
            x2 = x1 + random.randrange(int(self.canvas["width"]) / 2)
            y2 = y1 + random.randrange(int(self.canvas["height"]) / 2)
            self.canvas.create_rectangle(x1, y1, x2, y2)


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x50+200+300")
    app = Application(master=root)
    root.mainloop()
