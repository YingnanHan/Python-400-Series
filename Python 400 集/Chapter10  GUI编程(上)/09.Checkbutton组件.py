# coding:utf-8
"""测试Checkbutton组件的基本用法，使用面向对象的方式"""

from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)  # super()代表的是父类的定义，而不是父类对象
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.codeHobby = IntVar()
        self.videoHobby = IntVar()

        print(self.codeHobby.get())  # 默认值是0
        self.c1 = Checkbutton(
            self, text="敲代码", variable=self.codeHobby, onvalue=1, offvalue=0
        )
        self.c2 = Checkbutton(
            self, text="看视频", variable=self.videoHobby, onvalue=1, offvalue=0
        )

        self.c1.pack(side="left")
        self.c2.pack(side="left")

        Button(self, text="确定", command=self.confirm).pack(side="left")

    def confirm(self):
        if self.videoHobby.get() == 1:
            messagebox.showinfo("测试", "看视频，都是正常人有的爱好！你喜欢看什么类型？")
        if self.codeHobby.get() == 1:
            messagebox.showinfo("测试", "抓获野生程序猿一只，赶紧送给他尚学堂的视频充饥")


if __name__ == "__main__":
    root = Tk()
    root.geometry("400x50+200+300")
    app = Application(master=root)
    root.mainloop()
