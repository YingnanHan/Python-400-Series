import random

# sort函数可以对列表直接进行排序,并且不生成新的列表对象，直接在原有列表上操作

l = [210, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# 升序排列
print(id(l))
l.sort()
print(l)
print(id(l))
# 降序排列
print(id(l))
l.sort(reverse=True)
print(l)
print(id(l))
# 随机打乱列表
random.shuffle(l)
print(l)

# 内置函数sorted也会对l进行排序，但是会返回一个新的对象，并且不改变原来的列表
res = sorted(l)
print(res)
print(l is res)
