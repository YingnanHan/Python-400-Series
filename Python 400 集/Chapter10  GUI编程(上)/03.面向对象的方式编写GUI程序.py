# coding:utf-8
from tkinter import *
from tkinter import messagebox

'''
测试一个经典的GUI程序的写法，使用面向对象的方式
'''


class Application(Frame):  # 通用写法
    """
    一个经典的GUI程序的类的写法
    """

    # 构造器用于构建组件对象
    def __init__(self, master=None):
        super().__init__(master)  # 调用父类的构造方法
        self.master = master  # 为父类传参数初始化master
        self.pack()  # 作为一个组件调用布局管理器
        self.createWidget()  # 创建其他组件并且安装到Frame上

    def createWidget(self):
        """创建组件"""

        '''添加送花按钮'''
        self.btn01 = Button(self)  # 在当前容器上添加按钮,Frame上的组件的master是自己
        self.btn01["text"] = "点击送花"  # 设置按钮上的文字
        self.btn01["command"] = self.sendFlower  # 定义点击按钮后的动作
        self.btn01.pack()  # 通过布局管理器显示

        '''添加退出按钮'''
        self.btnQuit = Button(self, text="退出", command=self.master.destroy)  # 这里的destroy是直接关闭主窗口
        '''command=root.destroy :Destroy this and all descendants widgets. This will end the application of this Tcl interpreter.'''
        self.btnQuit.pack()

    # 定义单击送花按钮触发的事件
    def sendFlower(self):
        # 设置标题信息 & 文本内容
        messagebox.showinfo("送花", "送你一朵玫瑰花")


if __name__ == '__main__':
    # 创建根窗口对象
    root = Tk()
    root.geometry("400x100+200+300")
    # 编写标题
    root.title("A classcal GUI program!")
    # 在主串口里面新建立一个矩形区域
    app = Application(master=root)  # master用来将app与root挂钩
    # 调用事件的消息循环
    root.mainloop()
