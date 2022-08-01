# Case 01  空列表是false

b = []

if not b:
    print("空列表是false")

# Case 02 布尔值按本意

c = True
if c:
    print("c")

# Case 03 空字符串表示False
c = ""
if c:
    print(c)

# Case 04 非零数字为True
d = 10
if d:
    print(d)

# Case 05 非空字符串为True
s = "abc"
if s:
    print(s)

# #Case 06 赋值运算符不能出现在if判断语句中
# if a=1:
#     print(a)#SyntaxError: invalid syntax
