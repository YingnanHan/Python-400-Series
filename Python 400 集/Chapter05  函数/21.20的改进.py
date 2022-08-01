# 测试递归函数

def test01(n):  # 人为地设置递归函数的结束标记
    print("test01", n)
    if n == 0:  # 一旦满足退出条件，栈帧弹出系统栈，递归程序逐渐结束
        print("over")
    else:
        test01(n - 1)
    print("test01***", n)


def test02():
    print("test02")


test01(5)
