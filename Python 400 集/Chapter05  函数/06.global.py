# 测试全局变量与局部变量
# a = 3
# def test01():
#     b = 4           #局部变量，作用于仅限于函数内部，调用之后在内存中消失
#     print(b*10)     #在函数外部不能使用
#     a = 300         #这里的a与外部a是不一样的，这里的a存储在栈帧中而外部的a存储在堆中
#
# test01()
# print(a)
# #print(b)            #NameError: name 'b' is not defined

###  使用global标识符定义变量，是的函数内部使用的重名变量与外部的堆空间
###  中的变量是同一个变量的对象

a = 3
print(id(a))


def test01():
    b = 4  # 局部变量，作用于仅限于函数内部，调用之后在内存中消失
    print(b * 10)  # 在函数外部不能使用
    global a  # 说明这里的a与外部的a是同一个对象
    print(id(a))
    a = 300  # 这里的a与外部a是不一样的，这里的a存储在栈帧中而外部的a存储在堆中


test01()
print(a)
# print(b)            #NameError: name 'b' is not defined
