# coding=utf-8
# 列出工作目录录下所有的.py文件，并输出文件名

import os

path = os.getcwd()

file_list = os.listdir(path)  # 列出子目录以及子文件
for file in file_list:
    # 对每一个文件
    if file.endswith("py"):
        print(file)

print()
# 使用列表推导式
file_list_new = [filename for filename in file_list if filename.endswith(".py")]
for f in file_list_new:
    print(f)
