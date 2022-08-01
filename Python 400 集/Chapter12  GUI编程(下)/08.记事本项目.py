# coding:utf-8

from tkinter import *
from tkinter.dialog import *
from tkinter.colorchooser import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class Application(Frame):

    def __init__(self,master=None):

        super().__init__(master = master)
        self.master = master
        self.createWidgets()
        self.pack()


    def createWidgets(self):
        #创建主菜单栏
        menubar = Menu(self.master)

        #创建子菜单
        menuFile = Menu(menubar)
        menuEdit = Menu(menubar)
        menuHelp = Menu(menubar)

        #将子菜单加入到主菜单栏
        menubar.add_cascade(label="文件(F)",menu=menuFile)
        menubar.add_cascade(label="编辑(E)",menu=menuEdit)
        menubar.add_cascade(label="帮助(H)",menu=menuHelp)

        #增加菜单项           名称         快捷方式              触发函数
        menuFile.add_command(label="新建",accelerator="ctrl+n",command=self.newFile)
        menuFile.add_command(label="打开", accelerator="ctrl+o",command=self.openFile)
        menuFile.add_command(label="保存", accelerator="ctrl+s",command=self.saveFile)
        menuFile.add_separator()#添加分割线
        menuFile.add_command(label="退出", accelerator="ctrl+q",command=self.exit)

        #将主菜单栏加入到跟窗口
        self.master["menu"] = menubar

        #增加快捷键的处理
        root.bind("<Control-n>", lambda event: self.newFile())
        root.bind("<Control-o>", lambda event: self.openFile())
        root.bind("<Control-s>", lambda event: self.saveFile())
        root.bind("<Control-q>", lambda event: self.exit())
        #文本编辑区
        self.textpad = Text(self.master,width=50,height=30)
        self.textpad.pack()

        #创建上下文菜单
        self.contextMenu = Menu(self.master)
        self.contextMenu.add_command(label = "背景颜色",command = self.openAskColor)

        #为右键绑定事件
        self.master.bind("<Button-3>",self.createContextMenu)


    #新建文件
    def newFile(self):
        #文件的存储及其默认属性
        self.filename = asksaveasfilename(title="另存为",initialfile="未命名.txt",filetypes=[("文本文档","*.txt")],
                          defaultextension=".txt")
        self.saveFile()#保存文件


    #打开文件
    def openFile(self):
        self.textpad.delete(1.0,END)#把text控件中所有的内容清空
        with askopenfile(title="打开文本文件") as f:
            self.filename = f.name#保存文件名用于后续其他处理
            self.textpad.insert(INSERT,f.read())#将文件打开并将其中的文字插入到记事本中


    #保存文件
    def saveFile(self):
        with open(self.filename,"w") as f:
            #获得当前Text控件中所有的内容
            c = self.textpad.get(1.0,END)
            #将文本重新覆盖写入记事本打开的文件当中
            f.write(c)


    #退出程序
    def exit(self):
        #直接使用root下的quit()方法来退出函数
        self.master.quit()


    #修改文本编辑框的背景颜色
    def openAskColor(self):
        s1 = askcolor(color="red",title="选择背景色")
        self.textpad.config(bg=s1[1])#设置文本编辑区的属性

    def test(self):
        pass

    def createContextMenu(self,event):
        #菜单在鼠标右键单机的坐标处显示
        self.contextMenu.post(event.x_root,event.y_root)


if __name__ == '__main__':

    root = Tk()
    root.geometry("450x300+200+300")
    root.title("我的记事本")
    app = Application(root)
    root.mainloop()
