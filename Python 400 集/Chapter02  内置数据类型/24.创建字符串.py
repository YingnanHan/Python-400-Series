# 使用双引号或者单引号定义字符串

s = "text"  # 字符串的赋值与输出
print(s)
print("'I am a teacher!'")  # 如果字符串里面需要加上引号那么应当与包裹字符串本身的引号不同类型
print('"He is a student!"')

# 使用 """ """  或者 ''' '''来定义跨行的字符串
s = """
        这是一个跨行的字符串
        第一行
        第二行
"""
print(s)

# 使用 "" 或者 ''定义一个空字符串
s = ""
print("这里有一个空字符串{0}".format(s))
print("空字符串的长度为{0}".format(len(s)))
