# coding:utf-8

"""扑克牌游戏界面的设计"""

from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master):

        super().__init__(master=master)
        self.master = master
        self.createWidgets()
        self.pack()

    def createWidgets(self):
        """通过place布局管理器实现扑克牌的位置控制"""

        # 循环遍历所有的扑克牌图片
        self.photos = [
            PhotoImage(file="image/puke/puke" + str(1 + i) + ".gif") for i in range(10)
        ]
        self.puke = [Label(self.master, image=self.photos[i]) for i in range(10)]
        for i in range(10):
            self.puke[i].place(x=10 + i * 40, y=50)

        # 为所有的Label增加事件处理
        # 对所有的扑克牌对象当进行左键点击的时候执行self.chupai功能
        self.puke[0].bind_class("Label", "<Button-1>", self.chupai)

    # 处理扑克牌点击事件
    def chupai(self, event):
        # print(event.widget.winfo_geometry())#打印被点击处坐标
        print(event.widget.winfo_x(), end=" ")  # 获取被点击处的y坐标
        print(event.widget.winfo_y())  # 获取被点击处的x坐标
        # 制作出牌功能 当对某一个牌的点击事件发生时，修改其坐标

        # 注意：event.widget函数获得被点击的组件对象
        #    winfo_x winfo_y 用来获得屏幕上对象的位置
        #    对实际位置的修改只需要将这些对象重新放置，调用place即可
        if event.widget.winfo_y() == 30:
            """
            winfo_y(self):
                Return the y coordinate of the upper left corner of this widget
                in the parent.
            """
            event.widget.place(y=50)  # 出牌
        if event.widget.winfo_y() == 50:
            event.widget.place(y=30)  # 收回


if __name__ == "__main__":

    root = Tk()
    root.geometry("600x270+200+300")
    app = Application(root)
    root.mainloop()
