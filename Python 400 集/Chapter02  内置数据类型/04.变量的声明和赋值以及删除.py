a = 3  # a作为常量3的引用对象
print(a)
print(id(a))
del a  # 手动释放内存 实际上如果不再引用对象那么就会自动回收
print(a)  # 由于将对象a删除所有这里会报错  name 'a' is not defined
