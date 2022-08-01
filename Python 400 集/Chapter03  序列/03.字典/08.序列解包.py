# 序列解包可以方便的对左边的元素进行赋值
# 以任意方式定义等右边的序列
x, y, z = (1, 2, 3)
print(x, y, z)
(x, y, z) = (1, 2, 3)
print(x, y, z)
x, y, z = {1: 'a', 2: 'b', 3: 'c'}.keys()
print(x, y, z)
x, y, z = {1: 'a', 2: 'b', 3: 'c'}.values()
print(x, y, z)
x, y, z = {1: 'a', 2: 'b', 3: 'c'}.items()
print(x, y, z)
