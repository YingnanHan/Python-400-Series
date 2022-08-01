#使用装饰器完成不修改func1  func2的源码，添加输出日志信息
import time
def writeLog(func):
    try:
        file = open("log.txt","a",encoding="utf-8")
        file.write("访问函数")
        file.write(func.__name__)
        file.write("\t")
        file.write("时间 ")
        file.write(time.asctime())
        file.write("\n")

    except Exception as e:
        print(e.args)

    finally:
        file.close()

#使用闭包实现对简单函数添加闭包
def outer(func):
    def inner():
        writeLog(func)
        func()
    return inner

#为func1添加装饰器 构造闭包
@outer
#在解释执行的时候会发现有一个装饰器outer,那么python就会将func1作为函数outer
#的参数传入 当调用func1的时候执行闭包功能 函数的执行顺序为 outer -> inner->
# writeLog->func1
def func1():
    print("function1")

#为func2添加装饰器 构造闭包
@outer
def func2():
    print("function2")

#闭包的使用
'''
实际上闭包是使用一条语句代替以下两条语句用的
func1 = funcOut(func1)
func1()
'''

func1()#这里已经作为闭包函数在使用了
func2()#这里已经作为闭包函数在使用了