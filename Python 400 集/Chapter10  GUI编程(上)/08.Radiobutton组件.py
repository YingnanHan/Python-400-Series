# coding:utf-8
"""测试Radiobutton组件的基本用法，使用面向对象的方式"""

from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)  # super()代表的是父类的定义，而不是父类对象
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.v = StringVar()
        self.v.set("F")
        # 绑定同一个值，就会导致互斥
        self.r1 = Radiobutton(self, text="男性", value="M", variable=self.v)
        self.r2 = Radiobutton(self, text="女性", value="F", variable=self.v)

        self.r1.pack(side="left")
        self.r2.pack(side="left")

        Button(self, text="确定", command=self.confirm).pack(side="left")

    def confirm(self):
        messagebox.showinfo("测试", "选择的性别:" + self.v.get())


if __name__ == "__main__":
    root = Tk()
    root.geometry("400x50+200+300")
    app = Application(master=root)
    root.mainloop()
