from threading import Thread,Lock
from queue import Queue
import time

class Producer(Thread):

    def run(self):
        global queue
        count = 0   #产品数量
        while True:
            #判断队列的大小
            if queue.qsize()<1000:#设定生产条件
                for i in range(100):#一次性生产100件产品
                    count+=1
                    msg = "生产第{0}号产品".format(count)
                    queue.put(msg)#将产品放入队列
                    print(msg)#打印相应的生产信息


class Consumer(Thread):

    def run(self) :
        global queue
        while True:
            if queue.qsize()>100:
                for i in range(10):
                    #消费产品
                    msg = self.name + "消费产品,编号为" + queue.get()
                    print(msg)
                time.sleep(1)
if __name__ == '__main__':
    queue = Queue()#定义一个消息队列
    #创建生产者
    p = Producer()
    c = Consumer()

    p.start()
    time.sleep(1)
    c.start()