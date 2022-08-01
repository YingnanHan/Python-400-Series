# 定义方式一

# 当元祖元素只有一个的时候第一个元素后面必须加逗号，否则会被理解为一个数
a = 1
print(type(a))
a = (1,)
print(type(a))

# 定义方式二
# 通过tuple方式创建
t = tuple()
print(t)

t = tuple("abcdef")  # 将字符串转化为元组
print(t)
