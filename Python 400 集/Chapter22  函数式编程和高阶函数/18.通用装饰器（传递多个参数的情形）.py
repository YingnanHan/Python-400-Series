def WriteLog(func):
    import time
    print("Access ：" + func.__name__ + str(time.asctime()))


def Out(func):
    def In(*args,**kwargs):
        WriteLog(func)
        return func(*args,**kwargs)
    return In

@Out
def sum(a,b):
    return a+b

@Out
def add(a,b,c):
    return a+b+c

result = sum(10,20)
print("两个数之和:",result)
result = add(10,20,30)
print("三个数之和：",result)