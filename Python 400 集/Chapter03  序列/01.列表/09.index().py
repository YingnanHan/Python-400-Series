# index() 获得指定元素在了列表中首次出现的索引
a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(a.index(10))
print(a.index(10, 2, 3))  # 限定从某处开始到某处结束的查找范围，如果没找到抛出异常
