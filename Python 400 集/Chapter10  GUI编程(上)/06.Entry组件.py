# coding=utf-8

'''
Entry 用来接收一行字符串的控件。如果用户输入的文字
长度长于 Entry 控件的宽度时, 文字会自动向后滚动。如果
想输入多行文本, 需要使用 Text 控件。
'''

# 测试Entry组件的基本使用方法，使用面向对象的方式

from tkinter import *
from tkinter import messagebox


class Application(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        """创建登录界面的组件"""

        # ---创建用户名输入框
        self.label01 = Label(self, text="用户名")
        self.label01.pack()

        # StringVar变量绑定到指定的组件
        # StringVar变量的值发生变化，组件内容也发生变化
        # 组件内容发生变化，StringVar变量的值也发生变化
        value1 = StringVar()  # 定义一个可接受文本输入框文字的对象
        self.entry01 = Entry(self, textvariable=value1)
        value1.set("admin")  # 指定对象在文本输入框里面的默认内容
        self.entry01.pack()
        # v=value1.get()#使用这个方法可以得到指定的文本框对象里面的内容
        # print(v)

        # ---创建密码输入框
        self.label02 = Label(self, text="密码")
        self.label02.pack()

        value2 = StringVar()  # 定义一个可接受文本输入框文字的对象
        self.entry02 = Entry(self, textvariable=value2, show="*")  # 使用*来代替输入的的内容
        self.entry02.pack()
        # v = value2.get()  # 使用这个方法可以得到指定的文本框对象里面的内容
        # print(v)

        self.btn01 = Button(self, text="登录", command=self.login)
        self.btn01.pack()

    def login(self):
        username = self.entry01.get()
        password = self.entry02.get()

        print("去数据库比对用户名和密码...")
        print("用户名:" + username)
        print("密码:" + password)

        if username == "dosdiosas" and password == "980665":
            messagebox.showinfo("STX学习系统", "登陆成功，欢迎开始学习！")
        else:
            messagebox.showinfo("STX学习系统", "登陆失败，用户名或密码错误")


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x130+200+300")
    app = Application(root)
    root.mainloop()
