# #定义函数1
# def func1():
#     print("function1")
#
# #定义函数2
# def func2():
#     print("func2函数正在执行")

#定义写日志方法
def Writelog(func):
    import time
    print("访问了方法:"+func.__name__+" 访问时间:"+str(time.time()))

#定义一个闭包  并且为内部函数传递参数
def Out(func):
    def In(x,y):
        Writelog(func)
        return func(x,y)#这里需要有返回值
    return In

#计算两个数字的和
@Out
def sum(a,b):
    return a+b

res = sum(1,2)
print(res)