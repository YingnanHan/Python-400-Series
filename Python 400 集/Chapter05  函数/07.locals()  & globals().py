# locals() 与 globals() 函数用于给出当前python文件中的
# 全局变量与局部变量都有哪些

###举例说明如下
a = 100


def f(a, b, c):
    print(a, b, c)
    print(locals())  # 首先输出当前脚本下的局部变量
    print("#" * 20)
    print(globals())  # 输出当前脚本下的全局变量


f(1, 2, 3)
