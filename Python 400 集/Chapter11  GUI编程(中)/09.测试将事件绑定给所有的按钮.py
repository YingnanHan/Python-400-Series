# coding:utf-8

from tkinter import *
from tkinter import messagebox

class Application(Frame):

    def __init__(self,master):

        super().__init__(master=master)
        self.master = master
        self.createWidgets()
        self.pack()

    def createWidgets(self):

        b1 = Button(self.master,text="测试bind()绑定")
        b1.pack(side = "left")
        b1.bind("<Button-1>",self.mouseTest1)

        b2 = Button(self.master,text="测试command2")
        b2.pack(side = "left")
        b2["command"] = lambda : self.mouseTest2("John","Mike")

        #给b1按钮绑定右键事件
        b1.bind_class("Button","<Button-2>",self.mouseTest3)

    def mouseTest1(self,event):
        print("bind()方式绑定，可以获取event对象")
        print(event.widget)

    def mouseTest2(self,a, b):
        print("a={0},b={1}".format(a, b))
        print("command方式绑定，不能直接获取event对象")

    def mouseTest3(event):
        print("右键单击事件，绑定给所有按钮啦！！")
        print(event.widget)


if __name__ == '__main__':

    root = Tk()
    root.geometry("270x30")
    app = Application(root)
    root.mainloop()