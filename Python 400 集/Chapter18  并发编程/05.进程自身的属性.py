# 本例程测试进程的pid

from multiprocessing import  Process
import time

#定义执行函数
def clock(interval):
    for i in range(5):
        print("当前时间为{0}".format(time.time()))
        time.sleep(interval)

if __name__ == '__main__':
    #请注意子进程在main进程里面的生命周期
    #创建进程
    p = Process(target=clock,args=(1,))
    print(p.is_alive())
    #启动进程
    p.start()
    print(p.is_alive())
    p.join()
    #获取进程的pid name alive属性
    print(p.pid)
    print(p.name)
    print(p.is_alive())