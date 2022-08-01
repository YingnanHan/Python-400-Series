"""通用消息框"""

from tkinter.simpledialog import *
from tkinter import *
from tkinter.messagebox import *

class Application(Frame):

    def __init__(self, master):
        super().__init__(master=master)
        self.master = master
        self.createWidgets()
        self.pack()

    def createWidgets(self):
        self.s = showinfo(title="SXT",message="从零开始，深入底层，深入算法，打好基础")

if __name__ == '__main__':
    root = Tk()
    root.geometry("400x100+200+200")
    app = Application(root)
    root.mainloop()