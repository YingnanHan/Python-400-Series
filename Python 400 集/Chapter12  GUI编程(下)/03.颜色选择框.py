# coding:utf-8

# 测试颜色选择框

from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser


class Application(Frame):

    def __init__(self, master):
        super().__init__(master=master)
        self.master = master
        self.createWidgets()
        self.pack()

    def createWidgets(self):
        self.btn01 = Button(self.master, text="选择背景颜色", command=self.test)
        self.btn01.pack()

    def test(self):
        # 定义一个颜色选择框的对象，设置默认选择的颜色，以及选择框标题
        s = colorchooser.askcolor(color="red", title="选择背景颜色")
        print(s)  # 输出当前所选择的颜色对象
        self.master.config(bg=s[1])  # 设置当前选框的背景颜色为所选颜色


if __name__ == '__main__':
    root = Tk()
    root.geometry("200x200")
    app = Application(master=root)
    root.mainloop()
