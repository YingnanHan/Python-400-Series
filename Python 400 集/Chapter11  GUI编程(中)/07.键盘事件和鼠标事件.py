# coding:utf-8

#测试键盘事件和鼠标事件

from tkinter import *
from tkinter import messagebox

class Application(Frame):

    def __init__(self,master):
        super().__init__(master = master)
        self.master = master
        self.createWidgets()
        self.pack()

    def createWidgets(self):
        #设置一张画布
        self.c1 = Canvas(self.master,width = 200,height = 200,bg = "green")
        self.c1.pack()

        self.c1.bind("<Button-1>",self.mouseTest)
        self.c1.bind("<B1-Motion>",self.dragTest)

        self.master.bind("<KeyPress>",self.keyboardTest)
        self.master.bind("<KeyPress-a>",self.press_a_test)
        self.master.bind("<KeyRelease-a>",self.release_a_test)

    #定义事件
    def mouseTest(self,event):
        print("鼠标左键点击位置(相对于父容器)：{0},{1}".format(event.x,event.y))
        print("鼠标左键点击位置(相对于屏幕)：{0},{1}".format(event.x_root,event.y_root))
        print("事件绑定的组件:{0}".format(event.widget))

    def dragTest(self,event):
        self.c1.create_oval(event.x,event.y,event.x+10,event.y+10)

    def keyboardTest(self,event):
        print("按键的keycode:{0},按键的char:{1},按键的keysym:{2}".format(event.keycode,event.char,event.keysym))

    def press_a_test(self,event):
        print("press a")

    def release_a_test(self,event):
        print("release a")



if __name__ == '__main__':

    root = Tk()
    root.geometry("530x300")
    app = Application(root)
    root.mainloop()

