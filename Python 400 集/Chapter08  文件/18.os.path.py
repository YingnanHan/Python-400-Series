# coding=utf-8

import os
import os.path as path

# 判断：绝对路径，是否目录，是否文件，文件是否存在

print(os.path.isabs("# coding=utf-8"))  # 判断是否为绝对路径
print(os.path.isfile("18.os.path.py"))  # 判断是否为文件
print(os.path.isdir("./file"))  # 判断是否为路径
print(os.path.exists("01.文本文件的写入.py"))  # 判断文件是否存在

# 获得文件的基本信息
print(os.path.getsize("./file/a.txt"))  # 获得文件大小
print(os.path.abspath("./file/a.txt"))  # 获得文件的绝对路径的大小
print(os.path.dirname("./file/a.txt"))  # 输出文件所在目录

print(os.path.getctime("./file/a.txt"))  # 返回创建时间
print(os.path.getatime("./file/a.txt"))  # 返回最后访问时间
print(os.path.getmtime("./file/a.txt"))  # 返回最后修改时间

# 关于文件路径的操作
path = os.path.abspath("./file/b.txt")
print(os.path.split(path))  # 将文件的绝对路径划分为路径和文件名
print(os.path.splitext(path))  # 按照.来对文件路径进行切割
print(os.path.join("aa", "bb", "cc"))  # 按照系统文件的连接符链接
