# 使用 [] 创建列表
s = [10, 20, "Mike", "John"]
# 使用 list 创建列表
d = list()  # 创建空的列表对象
e = list("abcdefgh")  # 将其他类型对象转化为列表
f = list(range(10))  # 将整数序列对象转化为列表
# 使用range(start,end,step)创建列表
g = list(range(0, 10, 2))
h = list(range(3, 100, 15))
i = list(range(20, 3, -1))  # 倒序生成列表
# 推导式生成列表
j = [x * 2 for x in range(5)]
k = [x * 2 for x in range(100) if x % 2 == 0]

print(s)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
