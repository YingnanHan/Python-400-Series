import time
from threading import Thread

#定义一个全局变量
num = 10

def Deftest1():
    global  num
    for i in range(3):
        num += 1
    print("test1 num:{0}".format(num))

def Deftest2():
    print("执行test2，num的值为",num)

if __name__ == '__main__':
    #创建线程
    t1 = Thread(target=Deftest1)
    t2 = Thread(target=Deftest2)
    t1.start()
    t1.join()#保诚t1对全局变量修改之后t2在进行操作
    t2.start()
    t2.join()