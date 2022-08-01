from multiprocessing import Process
import os
from time import sleep

#传递子进程参数 并且在main中获取并输出
def run_proc(name,**kwargs):
    print("子进程运行中",end=" ")
    print("name:",name,end=" ")
    print("关键字参数列表：",kwargs)

if __name__ == '__main__':
    print("子进程开始执行")
    #创建子进程  注意：传递参数的时候必须要申明参数是属于哪种类型的 比如args 还是 kwargs并且需要用对应的类型来传参
    #                 在传递非关键字参数的时候含有一个元素的元组需要加上逗号
    #p = Process(target=run_proc,args=("test",),kwargs={'key':100})#字典值可以传递也可以不传递
    p = Process(target=run_proc,args=("test",),kwargs={'key':100,'age':19})#字典值可以传递也可以不传递
    #调用刚刚创建好的子进程
    p.start()