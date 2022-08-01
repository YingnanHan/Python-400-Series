# 本测试用于比较+ 与join函数在拼接字符串使得效率

import time

# 使用+拼接字符串
time01 = time.time()  # 起始时间

s = ""

for i in range(100000):
    s += "str"

time02 = time.time()
print("delta={0}".format(time02 - time01))


# 使用join拼接字符串
l = []
for i in range(100000):
    l.append("str")

time01 = time.time()  # 起始时间

s = ""
s = "".join(l)

time02 = time.time()
print("delta={0}".format(time02 - time01))
