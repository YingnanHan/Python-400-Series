import time
from threading import Thread,Lock

num=0

#创建一个互斥锁 将num变量在循环修改的时候锁住
lock = Lock()#生成一个锁对象

def Test1():
    global num
    lock.acquire()#将num变量锁住，num此时变为临界资源
    for i in range(1000000):
        num+=1
    print('test1输出num:',num)
    lock.release()#释放锁

def Test2():
    global num
    lock.acquire()
    for i in range(1000000):
        num+=1
    print('test2输出num:',num)
    lock.release()

if __name__=='__main__':
    t1=Thread(target=Test1)
    t2=Thread(target=Test2)
    t1.start()
    t2.start()
    #主线程等待两个子线程执行完毕
    t1.join()
    t2.join()
