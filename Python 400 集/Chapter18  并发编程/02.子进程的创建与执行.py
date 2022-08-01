from multiprocessing import Process

#定义子进程代码
def sub_test():
    print("function test running")

if __name__ == '__main__':
    print("进程main")
    #创建子进程 使用target参数来接收需要执行的进程
    p = Process(target=sub_test)
    p.start()#调用test进程