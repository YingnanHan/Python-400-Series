#闭包的特殊用途:
#       闭包可以在不修改源代码的前提下，为原函数增加新功能
import time
def writeLog(func):
    try:
        file = open("writeLog.txt",'a',encoding="utf-8")
        #向文件中写入日志信息  访问 方法名 时间
        file.write("访问:{0}".format(func.__name__))
        file.write("\t时间:{0}".format(time.asctime()))
        file.write("\n")

    except Exception as e:
        print(e)
    finally:
        file.close()

# #举例  添加日志功能
# def func1():
#     writeLog(func1)
#     print("function1")
#
# def func2():
#     writeLog(func2)
#     print("function2")
# #尽管实现了相应的功能，但实际上修改了我们函数本来的函数
# func1()
# func2()

#使用闭包在不修改原函数代码的条件下实现上述功能
def funcOut(func):
    def funcIn():
        #在内部调用功能函数并且写入日志
        writeLog(func)
        func()
        print("调用函数"+str(func.__name__)+"结束")
    return funcIn

def func1():
    print("fucntion1")

def func2():
    print("fucntion2")

#调用闭包的内部函数
func1 = funcOut(func1)
func1()

func2 = funcOut(func2)
func2()