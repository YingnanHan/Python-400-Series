# coding=utf-8
# 测试csv文件的读取
import csv

with open("file/test.csv", "r")as f:
    # 获得csv文件的内容得到一个读对象
    a_csv = csv.reader(f)
    print(a_csv)
    # 得到结果列表
    # print(list(a_csv))#用过一次文件的指针就回到末尾
    # 遍历csv中的内容
    for row in a_csv:
        print(row)
