# 测试嵌套函数（内部函数）的定义

def outer():
    print("outer running!!")

    def inner():  # 这个函数只能在函数内部使用，并不是一个全局的函数对象
        print("inner running!!")

    inner()


outer()
