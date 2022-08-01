# lambda表达式用来声明匿名函数，lambda表达式是一种简单的在同一行中定义的函的方法
# lambda表达式实际上产生了一种函数对象，lambda表达式只允许包含一个表达式，不可以
# 包含复杂的语句，该表达式计算的结果就是函数的返回值，lambda表达式的基本语法如下：
#               lambda     arg1，...argn :<表达式>
# arg1，...argn 为函数的参数，<表达式>相当于函数体，运算结果是函数的返回值

f = lambda a, b, c: a + b + c
print(f)  # 打印函数对象的地址
print(f(1, 2, 3))  # 实际调用lambda函数

g = [lambda a: a * 2, lambda b: b * 3, lambda c: c * 4]  # 这种类型的表达式传参数的时候可以将列表中的函数视作一个函数对象
print(g[0](1))
print(g[1](1))
print(g[2](1))
