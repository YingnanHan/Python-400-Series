# 一般来讲目前基本上使用format函数进行对字符串的格式化

# 通过以下例子来领会
s1 = "我的名字是:{0},年龄是:{1}".format("Mike", 18)  # 手动设置占位符
print(s1)
# 也可以使用位置参数进行赋值,这样不用考虑位置的问题
s1 = "我的名字是:{name},年龄是:{age}".format(age=18, name="Mike")  # 手动设置占位符
print(s1)
# 和上面是等价的
s1 = "我的名字是:{name},年龄是:{age}".format(name="Mike", age=18)  # 手动设置占位符
print(s1)
