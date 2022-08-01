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

        #定义滑块
        #滑块的值会当做参数传递给函数对象self.test1
        self.s1 = Scale(master=self.master,from_=10,to=50,length=200,tickinterval=5,orient=HORIZONTAL,command=self.test1)
        self.s1.pack()

        self.label = Label(master=self.master,text="ALOHA!",width=10,height=2,bg="black",fg="blue")
        self.label.pack()

    #从滑组里面获得的值可以通过一个参数v直接得到,并且这个参数必须存在
    def test1(self,v):
        #print(v)
        print("滑块的值：",self.s1.get())
        newFont = ("宋体",self.s1.get())

        self.label.config(font=newFont)

if __name__ == '__main__':

    root = Tk()
    root.geometry("400x400+200+200")
    app = Application(root)
    root.mainloop()