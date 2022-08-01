import threading
import time

def func1(delay):
    #threading.current_thread().getName()函数用来获取当前执行线程的名字
    print("线程{}执行func1".format(threading.current_thread().getName()))
    time.sleep(delay)
    print("线程{}执行结束".format(threading.current_thread().getName()))

def func2(delay):
    print("线程{}执行func2".format(threading.current_thread().getName()))
    time.sleep(delay)
    print("线程{}执行结束".format(threading.current_thread().getName()))

#创建一个MyThread类，继承threading.Thread
class MyThread(threading.Thread):
    #重写构造方法
    def __init__(self,func,name,args):
        #调用父类的构造方法初始化内容
        super(MyThread,self).__init__(target=func,name=name,args=args)

    #重写run方法
    def run(self):
        self._target(*self._args)#调用__init__()所传递进来的函数对象,并传递参数,执行
        #这里实际上就是为目标函数传递其所需要的参数
        
if __name__ == '__main__':
    print("开始运行")
    p1 = MyThread(func1,"thread-1",(2,))
    p2 = MyThread(func2,"thread-2",(4,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()