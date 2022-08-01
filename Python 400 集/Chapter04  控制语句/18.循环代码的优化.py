# 遵循原则
# 1.尽量减少循环内部的不必要的计算
# 2.循环嵌套中，尽量减少内层循环，尽可能向外提
# 3.局部变量查询较快，尽量使用局部变量

# 循环代码优化测试

import time

start = time.time()
for i in range(1000):
    result = []
    for m in range(10000):
        result.append(i * 1000 + m * 100)
end = time.time()
print("耗时:{0}".format(end - start))

start2 = time.time()
for i in range(1000):
    result = []
    c = i * 1000
    for m in range(10000):
        result.append(c + m * 10)

end2 = time.time()
print("耗时:{0}".format(end2 - start2))
