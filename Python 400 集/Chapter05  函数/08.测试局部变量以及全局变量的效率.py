# 测试局部变量与全局变量的效率

import math
import time


# 更加消耗时间
def test01():
    start = time.time()
    for i in range(1000000):
        math.sqrt(i)
    end = time.time()
    print("耗时{0}".format(end - start))


# 会提高一定的效率
def test02():
    b = math.sqrt  # 将函数对象作为全局变量使用
    start = time.time()
    for i in range(1000000):
        b(i)
    end = time.time()
    print("耗时{0}".format(end - start))


test01()
test02()
