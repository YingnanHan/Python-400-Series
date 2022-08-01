# in运算符

a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("a" in a)
print(1 in a)
print(10 in a)

# 使用count()运算符，如果返回值非零则元素存在反之不存在
print(a.count(100) > 0)
