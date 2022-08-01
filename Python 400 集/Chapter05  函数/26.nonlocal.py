# nonlocal 用来声明外层的局部变量
# global   用来声明全局变量

# 测试nonlocal global的用法

# case01
# def outer():
#     b = 10
#
#     def inner():
#         print("inner:",b)
#
#     inner()
#
# outer()

# case02  如果在内部inner函数中要修改b，那么首先要将b声明为nonlocal模式，表示
#        当前的修改并不是对内部函数对象b的引用的修改，而是外部函数的局部变量b
#        的修改

# def outer():
#     b = 10
#
#     def inner():
#         nonlocal b#声明外层函数的局部变量
#         b = 20
#         print("inner:",b)
#
#     print(b)
#     inner()
#     print(b)#可以发现b已经被内部函数修改
#
# outer()


# case03 声明使用全局变量
a = 0


def outer():
    b = 10

    def inner():
        nonlocal b  # 声明外层函数的局部变量

        print("inner:", b)
        b = 20

        global a  # 声明全局变量，也就是说下面所使用的a是定义在外部的a
        a = 1000  # 修改外部的a的值

    inner()
    print(b)  # 可以发现b已经被内部函数修改


outer()
print("a:", a)
