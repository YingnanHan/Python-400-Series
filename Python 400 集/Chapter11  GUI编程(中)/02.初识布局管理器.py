# coding:utf-8

from tkinter import *
from tkinter import messagebox


class Application(Frame):

    def __init__(self, master):
        super().__init__(master=master)
        self.master = master
        self.createWidgets()
        self.pack()

    def createWidgets(self):
        """通过布局管理器,实际上这里有些类似bootstrap的模式"""
        # 0行1列
        self.label01 = Label(self, text="用户名")
        self.label01.grid(row=0, column=0)
        # 0行1列
        self.entry01 = Entry(self)
        self.entry01.grid(row=0, column=1)
        # 0行2列
        Label(self, text="用户名默认为手机号").grid(row=0, column=2)
        # 1行0列
        Label(self, text="密码").grid(row=1, column=0)
        # 1行1列
        Entry(self, show="*").grid(row=1, column=1)
        # 2行1列             EW：登录按钮两侧拉长至当前格子最大限度
        Button(self, text="登录").grid(row=2, column=1, sticky=EW)
        # 2行2列             E ：取消按钮在当前单元格右侧对齐
        Button(self, text="取消").grid(row=2, column=2, sticky=E)


if __name__ == '__main__':
    root = Tk()
    root.geometry("")
    app = Application(master=root)
    root.mainloop()
