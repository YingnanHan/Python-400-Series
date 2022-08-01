# 语法格式
# for x in [可迭代对象]
#   循环体语句

# 测试for循环

# 元组
for x in (10, 20, 30):
    print(x)

# 字符串
for x in "abcdefg":  # 字符串也是可迭代对象
    # 等价于   for x in list("abcdefg"):
    print(x)

# 字典
d = {"name": "Mike", "age": 18, "job": "teacher"}
for x in d:  # 直接使用这种写法自动将键打印
    print(x)

# 上述写法同
for x in d.keys():  # 直接使用这种写法自动将键打印
    print(x)

# 打印出值
for x in d.values():  # 直接使用这种写法自动将值打印
    print(x)

# 打印字典本身
for x in d.items():  # 直接使用这种写法打印k-v对
    print(x)
