#定义函数foo 并且给其新增功能
#在foo函数前面 输出 I am foo

def Out(func):
    def In():
        print("I am ",func.__name__,end=" ")
        print()
        func()
    return In

@Out
def foo():
    print("foo正在运行")

foo()