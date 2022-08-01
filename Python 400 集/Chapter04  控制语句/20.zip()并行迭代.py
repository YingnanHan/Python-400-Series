# 测试并行迭代  指的是同时遍历多个可迭代对象

names = ("Mike", "John", "Joe", "Queen")
ages = (12, 13, 14, 14)
jobs = ("Teacher", "Student", "Police man")

# 并行迭代的次数以最短被迭代的列表长度为准
for name, age, job in zip(names, ages, jobs):
    print("{0}----{1}----{2}".format(name, age, job))
###############################################################
# 同样的他等价于
for i in range(3):
    print("{0}----{1}----{2}".format(names[i], ages[i], jobs[i]))
