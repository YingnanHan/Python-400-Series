#如果有三个或者三个以上的参数，那么么正确的装饰器模式如下

#定义写日志方法
def Writelog(func):
    import time
    print("访问了方法:"+func.__name__+" 访问时间:"+str(time.time()))

def Out(func):
    def In(x,y,z):
        Writelog(func)
        return func(x,y,z)
    return In

@Out
def add(a,b,c):
    return a+b+c

print(add(1,2,3))
