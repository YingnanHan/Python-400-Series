# 用于去除首尾特定信息
s = "**##abcdefg///##***"
s = s.strip("*")
print(s)
s = s.lstrip("#")
print(s)
s = s.rstrip("#")
print(s)
