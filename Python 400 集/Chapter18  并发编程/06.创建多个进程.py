from multiprocessing import Process
from time import  sleep

def work1(interval):
    print("work1 running...")
    sleep(interval)
    print("work1 end...")

def work2(interval):
    print("work2 running...")
    sleep(interval)
    print("work2 end...")

def work3(interval):
    print("work3 running...")
    sleep(interval)
    print("work3 end...")

if __name__ == '__main__':
    #调度之前已经设定好执行的次序
    print("main process running...")
    p1 = Process(target=work1, args=(4,))
    p2 = Process(target=work2, args=(2,))
    p3 = Process(target=work3, args=(3,))
    #调用子进程
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print("main process ends")