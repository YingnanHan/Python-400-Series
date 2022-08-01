#导入模块
from timeit import Timer

#定义append_test
def append_test():
    li=[]
    for i in range(10000):
        li.append(i)

def insert_test():
    li=[]
    for i in range(10000):
        li.insert(0,i)

#测试执行时间
append_timer=Timer('append_test()','from __main__ import append_test')
print('append插入执行时间：',append_timer.timeit(1000))

insert_timer=Timer('insert_test()','from __main__ import insert_test')
print('insert插入执行时间：',insert_timer.timeit(1000))