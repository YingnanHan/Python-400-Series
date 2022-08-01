# coding=utf-8

# 文件读取操作一般有以下几种形式
# 1. read([size])
# 从文件中读取 size 个字符，并作为结果返回。如果没有 size 参数，则读取整个文件。
# 读取到文件末尾，会返回空字符串。
# 2. readline()
# 读取一行内容作为结果返回。读取到文件末尾，会返回空字符串。
# 3. readlines()
# 文本文件中，每一行作为一个字符串存入列表中，返回该列表

# 操作一
with open(r"file/f.txt", "r", encoding="utf-8") as f:
    str = f.read()  # 将文件中的所有字符读取
    print(str)

print("----------------------------------------------------")
# 操作二
with open(r"file/f.txt", "r", encoding="utf-8") as f:
    str = f.read(10)  # 将文件中的前十个字符读取
    print(str)

print("----------------------------------------------------")
# 操作三
with open(r"file/f.txt", "r", encoding="utf-8") as f:
    while True:  # 使用循环每一次读取一行文件
        fragment = f.readline()
        if fragment != '':
            print(fragment)
        if not fragment:
            print("file end...")
            break

print("----------------------------------------------------")

# 操作四    #使用迭代器来操作文件
with open(r"file/f.txt", "r", encoding="utf-8") as f:
    for i in f:
        print(i, end="")
