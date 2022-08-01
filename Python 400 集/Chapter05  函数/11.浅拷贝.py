import copy

a = [10, 20, 30, 40, [50, 60, 70, 80]]
b = copy.copy(a)
print("a:", a)
print("b:", b)

b.append(30)
b[4].append(90)
print("浅拷贝......")  # 浅拷贝仅仅复制一份最外层列表对象，列表里面的嵌套内容会保留引用而不会复制
print("a:", a)
print("b:", b)
