# coding:utf-8

import csv

with open("file/k.csv", "w") as f:
    # 定义一个csv文件的写入对象
    r_csv = csv.writer(f)
    r_csv.writerow(["ID", "年龄", "姓名"])
    r_csv.writerow(["123", 15, "Mike"])

    # 也可以直接将一个二位列表写入
    c = [
        ["1234", 55, "John"],
        ["4567", 66, "Sarah"]
    ]
    r_csv.writerows(c)  # 注意如果这里使用writerow方法就会导致python解释器将
    # c看作是一个字符串直接写入
