#定义函数foo 并且给其新增功能
#在foo函数前面 输出 I am foo

def Out1(func):
    print("装饰器1")
    def In1():
        print("I am ",func.__name__,end="\n")
        func()
    return In1

def Out2(func):
    print("装饰器2")
    def In2():
        print("hello")
        func()
    return In2

@Out2   #在执行装饰器2
@Out1
def foo():
    print("foo正在运行")

foo()

'''
在函数定义阶段：执行顺序自下而上,定义阶段就是装饰器函数参数函数被调用之前(或者说内部函数之前的部分)
在函数执行阶段：执行顺序从上往下，一层层执行
'''