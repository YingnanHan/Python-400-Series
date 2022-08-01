"""文件对话框获取文件"""

from tkinter import  *
from tkinter.filedialog import *

root = Tk();root.geometry("400x100")


def test():
    f = askopenfilename(title="上传文件",initialdir="f:",filetypes=[("文本文件",".txt")])
    show["text"]=f


Button(root,text="选择编辑的文本文件",command=test).pack()

show = Label(root,width=40,height=3,bg="green")
show.pack()

root.mainloop()
