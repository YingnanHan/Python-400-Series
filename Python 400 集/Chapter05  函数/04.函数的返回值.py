# 测试返回值的基本用法

# 01返回一个值
def add(x, y):
    """
    计算两个数的和
    :param x:
    :param y:
    :return:
    """
    print("两数({0},{1})之和为{2}".format(x, y, x + y))
    return x + y


# 02return的作用
def test02():
    print("hello")
    return  # 这里的return的作用  1.返回值  2.结束函数的执行
    print("***")  # 这句话放在return后面不会被执行


# 03返回多个值的时候需要将多个值放到数据结构中
def test03(x, y, z):
    """
    将每一个参数加1，返回
    :param x:
    :param y:
    :param z:
    :return:
    """
    l = []
    l.append(x + 1)
    l.append(y + 1)
    l.append(z + 1)
    return l


add(10, 20)
test02()
print(test03(1, 2, 3))
