# 测试实参与形参

# 求解两个数字的最大值
def MaxValue(a, b):  # 在函数定义的时候定义的参数叫做形参，用于占位
    return a if a > b else b


print(MaxValue(10, 20))  # 这里的实参必须与形参数目相同，必须一一对应
