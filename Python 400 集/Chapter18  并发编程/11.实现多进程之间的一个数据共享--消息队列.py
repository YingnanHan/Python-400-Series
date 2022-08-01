#导入进程队列模块
from multiprocessing import Queue
#创建一个进程消息队列
q = Queue(3)#指定队列内部最大可存放元素的方法，如果不写，则没有大小限制
#向队列中插入消息
q.put("msg1")
q.put("msg2")
q.put("msg3")
#put方法中的可选参数
if not q.full():#通常在插入之前需要判断消息队列是否已满
    q.put("msg4",block=True,timeout=1) #指的是 如果队列已满那么就等待1s，如果1s过后消息队列还是满的就抛出异常
    '''
    抛出Full异常
    '''

#读取并删除元素 使用get方法
# print(q.get())
# print(q.get())
# print(q.get())
# if not q.empty():  #如果消息队列不为空
#     print(q.get(block=True,timeout=1))

#查看队列的大小
# print(q.qsize())

#获取消息队列中的消息
for i in range(q.qsize()):
    print(q.get())