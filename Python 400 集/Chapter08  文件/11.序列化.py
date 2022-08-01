# coding:utf-8
import pickle

# 序列化操作，将自定义字符串以二进制序列的形式写入文档
with open(r"file/i.txt", "wb")as f:
    s1 = "Hello"
    s2 = "\t"
    s3 = "world"
    s4 = "!"

    pickle.dump(s1, f)
    pickle.dump(s2, f)
    pickle.dump(s3, f)
    pickle.dump(s4, f)
