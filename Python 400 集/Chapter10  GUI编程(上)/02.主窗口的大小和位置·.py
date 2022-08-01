# coding:utf-8
from tkinter import *
from tkinter import messagebox

# 创建主窗口对象
root = Tk()
root.title("My first GUI project")  # 设置GUI窗口标题

# 设置主窗口的大小
root.geometry("500x300+100+200")  # 这句话的意思是，初始化的窗口的大小是500X300px 距离左侧100px距离上侧200Px

# 在主窗口安放组件
btn01 = Button(root)  # 创建一个按钮，安放在主窗口对象上
btn01["text"] = "点击送花"  # 在按钮上设置文字


# 定义绑定到按钮的事件
def sendFlower(e):
    # e:事件对象
    messagebox.showinfo("Massage", "送你一朵花！！")  # 调用messagebox.showinfo函数将文字显示在新弹出的窗口上
    print("送花成功")


# 将事件绑定到按钮
btn01.bind("<Button-1>", sendFlower)  # <Button-1>表示单击鼠标左键,第二个参数是事件触发后要执行的动作

# 调用布局管理器pack
btn01.pack()  # 将按钮合理的安装到窗口里面

# 调用mainloop方法，开启主事件循环，持续监听用户的操作
root.mainloop()
