# 方法一   del删除指定位置的元素,del函数实际上就是将被删除位置后面所有的元素向前挪动拷贝
l = [1, 2, 3, 4, 5, 6, 7]
del l[1]
print(l)

# 方法二   pop()删除并返回指定位置的元素，如果未指定则删除并返回列表中的最后一个位置的元素
l.insert(1, 2)
b = l.pop(2)
print(b)
print(l)

# 方法三  remove()删除首次出现的指定元素，不存在该元素则抛出异常
l = [10, 20, 30, 40, 50, 60, 70, 80, 90]
l.remove(20)
print(l)
