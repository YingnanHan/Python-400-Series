# 将目标列表的所有元素添加到本列表的尾部，属于原地操作，不会创建新的列表
# 就是在原有对象的基础上进行扩展
a = [12, 14]
print(id(a))
b = [13, 15]
print(id(b))
a.extend(b)
print(a)
print(id(a))
