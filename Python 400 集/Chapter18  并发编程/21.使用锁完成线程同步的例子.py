from threading import Lock,Thread
import time

#创建三把互斥锁
lockl = Lock()
lock2 = Lock()
lock3 = Lock()

#对lock2和lock3进行上锁
lock2.acquire()
lock3.acquire()

class Task1(Thread):
    def run(self):
        while True:
            if lockl.acquire():
                print("...task1...")
                time.sleep(1)
                #释放lock2的锁
                lock2.release()

class Task2(Thread):
    def run(self):
        while True:
            if lock2.acquire():
                print("...task2...")
                time.sleep(1)
                #释放lock3的锁
                lock3.release()


class Task3(Thread):
    def run(self):
        while True:
            if lock3.acquire():
                print("...task3...")
                time.sleep(1)
                #释放lock1的锁
                lockl.release()

if __name__ == '__main__':
    #本例子使用了锁来实现线程同步
    t1 = Task1()
    t2 = Task2()
    t3 = Task3()
    t1.start()
    t2.start()
    t3.start()