from multiprocessing import Manager,Pool
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
    q = Manager().Queue()
    #构造进程池
    pool = Pool(3)
    #设定进程之间的执行具有先后顺序
    pool.apply(write,(q,))
    pool.apply(read,(q,))
    #关闭进程池，并且开始执行进程池里面的进程
    pool.close()
    pool.join()
