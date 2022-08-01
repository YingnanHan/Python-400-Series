# coding=utf-8

# walk()用于递归遍历某一个文件目录中的文件和文件夹

import os

all_files = []
path = os.getcwd()
list_file = os.walk(path)

for dirpath, dirnames, filenames in list_file:
    for dir in dirnames:
        all_files.append(os.path.join(dirpath, dir))

    for file in filenames:
        all_files.append(os.path.join(dirpath, file))

# 打印所有的子目录和子文件
for file in all_files:
    print(file)
