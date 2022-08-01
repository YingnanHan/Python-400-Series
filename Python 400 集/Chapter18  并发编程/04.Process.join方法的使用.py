from multiprocessing import Process
from time import sleep

#定义任务函数
def task(intervals):
    print("processing task running...")
    sleep(intervals)
    print("processing ends")

if __name__ == '__main__':
    print("main process created")
    #创建子进程

    #case 01
    #创建子进程之后 主进程可能先执行完，但是由于其所创建的子进程没有执行完毕所以需要等待
    #p = Process(target=task,args=(3,))
    #p.start()

    #case 02
    #如果希望子进程之行结束之后再去执行返回点处的剩下的main的代码可以设置一定的等待时间
    #但是实际上子进程的执行时间并不是很好预估
    # p = Process(target=task,args=(3,))
    # p.start()
    # sleep(4)

    #case 03
    #使用join方法表示的是强制指定main进程在进程task之行结束之后在执行，相当于一个谦让
    # p = Process(target=task,args=(3,))
    # p.start()#一定要先让一个进程被分配PCB之后才可以
    # p.join()#can only join a started process

    #case 04
    #拒绝忙式等待 在join里面添加参数 当达到一定的时间限制后自动结束
    p = Process(target=task,args=(5,))
    p.start()
    p.join(timeout=3)#表示主进程仅仅等待子进程3s


    print("process main task ends")