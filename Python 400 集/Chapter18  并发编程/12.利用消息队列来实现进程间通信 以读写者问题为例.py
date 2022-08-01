from multiprocessing import *
import time

def write(q):
    #将列表元素的值写入队列中
    for i in [1,2,3]:
        print("开始写入值%d"%i)
        q.put(i)
        time.sleep(1)

def read(q):
    print("开始读取")
    while True:
        if not q.empty():
            print("读取到:",q.get())
            time.sleep(1)
        else:
            break

if __name__ == '__main__':
    #创建队列
    q = Queue()
    #创建写入进程
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    #启动进程  设定先写入在读取
    pw.start()
    pw.join()
    pr.start()
    pr.join()