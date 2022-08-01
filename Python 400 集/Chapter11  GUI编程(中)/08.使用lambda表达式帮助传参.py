# coding:utf-8

#测试command属性绑定事件，测试lambda表达式帮助传参

from tkinter import *
from tkinter import messagebox

class Application(Frame):

    def __init__(self,master):

        super().__init__(master=master)
        self.master=master
        self.createWidgets()
        self.pack()

    def createWidgets(self):
        btn01 = Button(self.master)
        btn01["text"] = "测试command01"
        btn01["command"] = self.mouseTest01
        btn01.pack(side = "left")

        btn02 = Button(self.master)
        btn02["text"] = "测试command02"
        btn02["command"] =lambda:self.mouseTest02("Mike","John")
        btn02.pack(side = "left")

    def mouseTest01(self):
        print("command方式，简单情况：不涉及获取event对象，可以使用")

    def mouseTest02(self,a,b):
        print("a={0},b={1}".format(a,b))
        print("lambda方式，含参情况：涉及获取event对象，可以使用")

if __name__ == '__main__':

    root = Tk()
    root.geometry("270x50")
    app = Application(root)
    root.mainloop()