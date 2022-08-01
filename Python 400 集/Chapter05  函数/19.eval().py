# eval()函数用于计算可以计算的str类型的表达式或者语句
s = "print('abcdefg')"
eval(s)

a = 10
b = 20
c = eval("a+b")
print(c)

# eval()对其他类型的对象进行操作
dict1 = dict(a=100, b=200)
d = eval("a+b")  # 默认情况下eval计算的是全局作用域中的a b之和
print(d)
d = eval("a+b", dict1)  # 如果指定来源，比如这里，就是计算dict1中的a b
print(d)
