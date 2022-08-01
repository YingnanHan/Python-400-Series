# coding:utf-8

from tkinter import *
from tkinter import messagebox


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        """创建组件"""

        # 设置组件的 所显示的文字  宽度  高度  背景色   前景色
        self.label01 = Label(self, text="S   X   T", width=20, height=2, bg="black", fg="white")
        self.label01.pack()

        self.label02 = Label(self, text="Mr.Qi Gao", width=20, height=2, bg="blue", fg="white", font=("黑体", 30))
        self.label02.pack()

        # 显示图片
        global photo  # 注意方法调用完毕之后photo对象就会消失，所以声明图片为global使得Tk一直可以使用photo对象防止图片不被显示出来
        photo = PhotoImage(file="image/logo.gif")  # 定义一个图片对象
        self.label03 = Label(self, image=photo)  # 使用iamge属性指定图片
        self.label03.pack()

        # 显示多行文本
        # 设置边框宽度 边框类型 多行文本对齐方式
        self.label04 = Label(self, text="北京尚学堂\n百战程序员",
                             borderwidth=1, relief="solid", justify="right")
        self.label04.pack()


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x400+200+300")
    root.title("测试Label")
    app = Application(master=root)
    root.mainloop()
