# 再带星号的“可变参数”后面增加新的参数，必须是“强制命名参数”
def f(*a, b, c):
    print(a, b, c)


# f(2,3,4)       #会报错，由于a是可变参数，会将参数2,3，4全部收集，造成实际上参数b c没有参数复制给他
f(2, b=3, c=4)  # 正确的写法，在调用的时候强制命名参数
f(2, b=3, c=4)  # 正确的写法，在调用的时候强制命名参数
