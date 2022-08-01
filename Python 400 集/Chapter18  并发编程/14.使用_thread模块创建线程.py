#方法一：使用_thread来实现线程
import _thread
import time

def func1():
    print("func1 start running...")
    time.sleep(4)
    print("func1 ending...")

def func2():
    print("func2 start running...")
    time.sleep(2)
    print("func2 ending...")

if __name__ == '__main__':
    print("main start running...")
    #创建线程
    _thread.start_new_thread(func1,())
    _thread.start_new_thread(func2,())
    time.sleep(7)#如果main函数不进行休眠，那么子线程就会被强行退出，等main执行结束之前func1&fun2未执行完毕
