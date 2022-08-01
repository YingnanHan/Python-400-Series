# 测试递归函数

def test01():
    print("test01")
    test01()


def test02():
    print("test02")


# 由此可见不可以无限制地调用哪个其他函数，这会导致栈空间溢出
# RecursionError: maximum recursion depth exceeded while calling a Python object
test01()
