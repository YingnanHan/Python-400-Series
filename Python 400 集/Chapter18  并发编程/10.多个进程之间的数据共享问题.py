from multiprocessing import  Process
#实际上这里应该涉及到一个同步互斥的PV操作问题
num = 10

def work1():
    global num
    num+= 5
    print("子进程1运行之后：num的值",num)

def work2():
    global num
    num+=10
    print("子进程2运行之后：num的值",num)

if __name__ == '__main__':

    #num的值是互相独立的，这种方法不能实现全局变量之间的共享

    print("主进程开始运行")
    #创建子进程
    p1 = Process(target=work1)
    p2 = Process(target=work2)
    #启动子进程
    p1.start()
    p2.start()
    #限制等待条件
    p1.join()
    p2.join()
    print(num)

