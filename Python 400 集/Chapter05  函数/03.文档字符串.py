# 函数的文档字符串使用 """ """
# 来定义用于说明函数的用途，参数的含义等信息

def print_star(num):
    """
    根据用户所传参数，打印对应数量的*
    :return:
    """
    for i in range(num):
        print("*", end="")


print()
print_star(100)
# 使用help函数来打印一个函数的文档注释
print(print_star.__doc__)  # 打印方法如左所示
