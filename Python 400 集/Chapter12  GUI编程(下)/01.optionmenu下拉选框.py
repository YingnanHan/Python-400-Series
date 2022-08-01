# coding:utf-8

from tkinter import *
from tkinter import messagebox

class Application(Frame):

    def __init__(self,master):

        super().__init__(master = master)
        self.master = master
        self.createWidgets()
        self.pack()

    def createWidgets(self):

        self.v = StringVar()
        self.v.set("清华大学")
        #定义一个下拉选框 参数为 绑定的父容器 选项的值的接受者  {选项列表}
        self.op = OptionMenu(self.master,self.v,"北京大学","西湖大学","清华大学")
        self.op["width"] = 10
        self.op.pack()

        self.btn = Button(self,text="Get",command=self.getVal)
        self.btn.pack()

    def getVal(self):
        print(self.v.get())
        return self.v.get()

if __name__ == '__main__':

    root = Tk()
    root.geometry("200x100")
    app = Application(master=root)
    print(app.v.get())
    root.mainloop()