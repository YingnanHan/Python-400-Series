a = {'name': 'Mike', 'age': 18, 'job': 'teacher'}
# 方式一  del
del (a['age'])
print(a)

# 方式二  pop
a.pop("job")  # 其返回值是对应键的值
print(a)

# 方式三 clear
a.clear()
print(a)

a = {'name': 'Mike', 'age': 18, 'job': 'teacher'}
# 方式四 popitem  随机移除元素
a.popitem()
print(a)
