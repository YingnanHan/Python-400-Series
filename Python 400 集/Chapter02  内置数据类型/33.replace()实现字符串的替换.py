# replace英语实现字符串的替换，并将替换后的内容做为新对象返回

s = "你好，Mike！"
r = s.replace("Mike", "John")
print(r)

# 这两个字符串不是一个对象
print(id(s))
print(id(r))
