class Queue:
    def __init__(self):
        self.__list=[]

    #进队
    def enqueue(self,item):
        # self.__list.append(item)
        self.__list.insert(0,item)

    #出队
    def dequeue(self):
        # return self.__list.pop(0)
        return self.__list.pop()

    #判断队列是否为空
    def is_empty(self):
        return self.__list == []

    #计算队列的大小
    def size(self):
        return len(self.__list)

if __name__ == '__main__':
    queue=Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    #判断队列是否空
    print(queue.is_empty())
    print('队列大小',queue.size())
    print('-----出队---------')
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())