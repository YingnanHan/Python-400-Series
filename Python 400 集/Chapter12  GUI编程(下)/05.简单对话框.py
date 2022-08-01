"""简单对话框"""

from tkinter.simpledialog import *
from tkinter import *
from tkinter import messagebox

class Application(Frame):

    def __init__(self, master):
        super().__init__(master=master)
        self.master = master
        self.createWidgets()
        self.pack()

    def createWidgets(self):

        self.btn = Button(self.master,text="请输入你的年龄:",command=self.test)
        self.btn.pack()
        self.label = Label(self.master,width=401,height=3,bg="green")
        self.label.pack()

    def test(self):
        #从对话框中获得一个整数对象回答
        #                弹出框标题             弹出框内部询问标题        输入栏初始值     可输入的最大值与最小值
        ask = askinteger(title="请输入你的年龄:",prompt="请输入你的年龄:",initialvalue=18,minvalue=1,maxvalue=150)
        #注意 对于askfloat  askstring的使用方式类似
        #将输入框中的内容显示到label中
        self.label["text"] = ask



if __name__ == '__main__':
    root = Tk()
    root.geometry("400x100+200+200")
    app = Application(root)
    root.mainloop()