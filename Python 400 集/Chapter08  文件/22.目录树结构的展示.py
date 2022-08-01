# coding=utf-8
# 递归打印所有的目录文件

import os

allFiles = []


def getAllFiles(path, level):
    childFiles = os.listdir(path)

    for file in childFiles:
        filepath = os.path.join(path, file)
        allFiles.append(level * "\t" + filepath)
        if os.path.isdir(filepath):
            getAllFiles(filepath, level + 1)


getAllFiles("H:\Python 400 集", 0)

for f in allFiles:
    print(f)
