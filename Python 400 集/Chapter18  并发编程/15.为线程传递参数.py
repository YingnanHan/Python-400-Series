import _thread
import time

def func1(thread_name,delay):
    print("开始运行func1,线程名称为:",thread_name)
    time.sleep(delay)
    print("运行func1结束")

def func2(thread_name,delay):
    print("开始运行func2,线程名称为:",thread_name)
    time.sleep(delay)
    print("运行func2结束")

if __name__ == '__main__':
    print("开始运行")
    #创建线程
    _thread.start_new_thread(func1,("thread-1",3))
    _thread.start_new_thread(func2,("thread-2",3))
    time.sleep(7)#主线程休眠7s，等待子进程执行结束