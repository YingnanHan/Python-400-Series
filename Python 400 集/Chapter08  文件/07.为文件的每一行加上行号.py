# coding=utf-8

# enumeration函数将一个列表中的每一个元素与序号组合成一个新的元组，进而将这些
# 元组合并为一个新的列表

# 测试部分内容
# l = ["My"," Name"," is"," Mike."]
# b = enumerate(l)
# print(b)#enumerate可以得到一个枚举对象
# print(list(b))
# #通过推导式生成列表
# c = [temp.strip()+"#"+str(index) for index,temp in enumerate(l)]
# print(c)


# 正式操作
with open("file/e.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    lines = [line.rstrip() + " #" + str(index) + "\n" for index, line in enumerate(lines)]

with open("file/e.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)
