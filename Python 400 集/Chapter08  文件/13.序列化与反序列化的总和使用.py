# coding=utf-8

import pickle

s1 = "Mike"
s2 = "18"
s3 = ["juice", "milk", "water"]

with open("file/j.txt", "wb") as f:
    pickle.dump(s1, f)
    pickle.dump(s2, f)
    pickle.dump(s3, f)

with open("file/j.txt", "rb") as f:
    b1 = pickle.load(f)  # 每一次load会执行一行文件的反序列化
    b2 = pickle.load(f)
    b3 = pickle.load(f)

    print(b1)
    print(b2)
    print(b3)
