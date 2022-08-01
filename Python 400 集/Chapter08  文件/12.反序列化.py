# coding:utf-8
import pickle

# 反序列化操作
with open(r"file/i.txt", "rb")as f:
    s1 = pickle.load(f)
    s2 = pickle.load(f)
    s3 = pickle.load(f)
    s4 = pickle.load(f)

print(s1)
print(s2)
print(s3)
print(s4)
