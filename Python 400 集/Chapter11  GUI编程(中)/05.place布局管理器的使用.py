# coding=utf-8

from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master):
        super().__init__(master=master)
        self.master = master
        self.createWidgets()
        self.pack()

    def createWidgets(self):
        # 相对位置均是按照实际的比例来配置的
        f1 = Frame(self.master, width=200, height=200, bg="green")
        f1.place(x=30, y=40)

        btn01 = Button(self.master, text="SXT")
        btn01.place(relx=0.2, rely=0.7)

        btn02 = Button(f1, text="Baizhan Programmer!")
        btn02.place(relx=0.6, rely=0.7)

        btn03 = Button(f1, text="GaoQi")
        btn03.place(relx=0.5, rely=0.2)


if __name__ == "__main__":
    root = Tk()
    root.geometry("400x400+200+200")
    app = Application(root)
    root.mainloop()
