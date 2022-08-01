import time
from threading import *
#定义全局变量num
#如果多个线程同时对同一个全局变量操作，会出现资源竞争问题，从而数据结果会不正确
num=0
def Test1():
    global num
    for i in range(1000000):
        num+=1
    print('test1输出num:',num)

def Test2():
    global num
    for i in range(1000000):
        num+=1
    print('test2输出num:',num)

if __name__=='__main__':
    t1=Thread(target=Test1)
    t2=Thread(target=Test2)
    t1.start()
    t2.start()
    #主线程等待两个子线程执行完毕
    t1.join()
    t2.join()
'''
原理：
    一个程序在未运行完全时就被停止而执行另一个程序了，从而导致这样的结果
    假设两个线程 t1 和 t2 都要对全局变量 g_num (默认是0)进行加1运算，t1 
    和 t2 都各对 g_num 加10次，g_num 的最终的结果应该为20。但是由于多线
    程是同时操作，有可能出现下面情况：在 g_num=0 时，t1 取得 g_num=0。此
    时系统把 t1 调度为”sleeping”状态，把t2转换为”running”状态，t2 也
    获得 g_num=0。***然后 t2 对得到的值进行加1并赋给 g_num***，使得 g_nu
    m=1 。接着系统又把 t2 调度为”sleeping”，把 t1 转为”running”。线程
    t1又把它之前得到的0加1后赋值给g_num。这样导致虽然 t1 和 t2 都对 g_num
    加1，但结果仍然是 g_num=1
'''