#导入模块
from multiprocessing import Process
from time import *

#定义类  这里和管程的构造相似
class ClockProcess(Process):
    #重写初始化方法
    def __init__(self,interval):
        Process.__init__(self)
        self.interval = interval

    #重写run方法
    def run(self):
        print("子进程开始执行的时间{0}".format(ctime()))
        sleep(self.interval)
        print("子进程结束执行的时间{0}".format(ctime()))

if __name__ == '__main__':
    #创建子进程
    p = ClockProcess(3)
    p.start()
    p.join()
    print("main Process ends")

#步骤
'''
1.定义一个进程类并且继承Process
2.重写run方法 将所有的当前需要执行的任务编写在run()里面
3.创建子进程类对象 并且调用start()方法
'''