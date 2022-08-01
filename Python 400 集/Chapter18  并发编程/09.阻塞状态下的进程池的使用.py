#导入模块
import multiprocessing
import time

#进程执行的任务函数
def func(msg):
    print("start:",msg)
    time.sleep(3)
    print("end:",msg)

if __name__ == '__main__':
    #创建初始化大小为3的非阻塞进程池
    pool = multiprocessing.Pool(3)
    #为进程池添加任务
    for i in range(6):
        msg = "任务%d"%i
        #添加完任务以后直接执行
        pool.apply(func,(msg,))#第一个参数用来传递进程标签，第二个参数用于传递参数


    #如果进程池不再接受新的任务申请，直接调用close
    pool.close()
    #主进程结束之后应当等待子进程的结束 这种等待是由子进程发起的
    pool.join()