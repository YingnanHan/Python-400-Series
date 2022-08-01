# coding:utf-8

# 计算器软件界面的设计

from tkinter import *
from tkinter import messagebox


class Application(Frame):

    def __init__(self, master):
        super().__init__(master=master)
        self.master = master
        self.createWidgets()
        self.pack()

    def createWidgets(self):

        # 通过grid布局管理器来实现一个计算器的界面
        btnText = (
            ("MC", "M+", "M-", "MR"),
            ("C", "±", "÷", "×"),
            (7, 8, 9, "-"),
            (4, 5, 6, "+"),
            (1, 2, 3, "="),
            (0, "."))

        # 生成一个文本框 向右横跨4列  pady表示距离上面的框10单位
        Entry(self).grid(row=0, column=0, columnspan=4, pady=10)

        for rindex, r in enumerate(btnText):
            for cindex, c in enumerate(r):
                # 注意在编写python程序的时候尽可能地使用elif而不是else if，否则会出现各种意想不到的问题
                if c == "=":
                    Button(self, text=c, width=2).grid(row=rindex + 1, column=cindex
                                                       , rowspan=2, sticky=NSEW)
                elif c == 0:
                    Button(self, text=c, width=2).grid(row=rindex + 1, column=cindex
                                                       , columnspan=2, sticky=NSEW)
                elif c == ".":
                    Button(self, text=c, width=2).grid(row=rindex + 1, column=cindex + 1
                                                       , sticky=NSEW)
                else:
                    Button(self, text=c, width=2).grid(row=rindex + 1, column=cindex
                                                       , sticky=NSEW)


if __name__ == '__main__':
    root = Tk()
    root.geometry("200x200+200+300")
    app = Application(root)
    root.mainloop()
