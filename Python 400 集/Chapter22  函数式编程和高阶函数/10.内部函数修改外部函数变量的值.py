def Outer(num1):
    def Inner(num2):
        nonlocal num1
        num1 += 1#在内部函数使用外部函数变量的时候需要显示声明为nonlocal
        return num1+num2
    return Inner

In = Outer(1)
res = In(2)
print(res)