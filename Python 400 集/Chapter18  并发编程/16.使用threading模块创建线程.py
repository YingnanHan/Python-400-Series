#使用threading.thread模块来创建线程的方式与进程的创建方式相似
#导入模块
import threading
import time

#定义要被执行的函数
def func1(thread_name,delay):
    print("线程{}开始执行func1".format(thread_name))
    time.sleep(delay)
    print("线程{}运行func1完毕".format(thread_name))

def func2(thread_name,delay):
    print("线程{}开始执行func2".format(thread_name))
    time.sleep(delay)
    print("线程{}运行func2完毕".format(thread_name))

if __name__ == '__main__':
    print("开始运行")
    t1 = threading.Thread(target=func1, args=("thread-1", 2))
    t2 = threading.Thread(target=func2, args=("thread-2", 2))
    #启动线程
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    #值得注意的是具体哪一个线程优先执行完毕这需要看处理机的调度方式