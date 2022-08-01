# coding:utf-8

# 测试pack布局管理器

from tkinter import *
from tkinter import messagebox


class Application(Frame):

    def __init__(self, master):
        super().__init__(master=master)
        self.master = master
        self.createWidgets()
        self.pack()

    def createWidgets(self):

        # Frame是一个矩形区域可以用来存放其他组件
        f1 = Frame(self.master)
        f1.pack()  # 默认设置垂直排列

        f2 = Frame(self.master)
        f2.pack()  # 默认设置垂直排列

        btnText = ["流行风", "中国风", "日本风", "重金属", "轻音乐"]

        for btn in btnText:
            Button(f1, text=btn).pack(side="left", padx="10")

        for i in range(1, 20):
            # 设计10个label水平排布
            Label(f2, width=5, height=10, borderwidth=1, relief="solid", bg="black" if i % 2 == 0 else "white").pack(
                side="left", padx=2)


if __name__ == '__main__':
    root = Tk()
    root.geometry("700x200+200+300")
    app = Application(root)
    root.mainloop()
