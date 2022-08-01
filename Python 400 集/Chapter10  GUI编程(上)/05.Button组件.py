# coding:utf-8

'''
测试Button组件的用法，基于面向对象的方式
'''

from tkinter import *
from tkinter import messagebox


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.createWidgets()
        self.pack()

    def createWidgets(self):
        # anchor表示text在父元件的相对位置
        self.btn01 = Button(self.master, text="login", width=6, height=3, anchor=E, command=self.login)
        self.btn01.pack()

        global photo
        photo = PhotoImage(file="image/start.gif")
        self.btn02 = Button(self.master, image=photo, command=self.login)
        self.btn02.config(state="disabled")  # 设置按钮为禁用
        self.btn02.pack()

    def login(self):
        messagebox.showinfo("登陆成功")


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x300+200+300")
    app = Application(master=root)
    root.mainloop()
