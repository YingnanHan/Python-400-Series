# coding=utf-8
with open("file/h.jpg", "rb")as f:
    with open("file/h_copy.jpg", "wb") as w:
        for line in f.readlines():
            w.write(line)

print("拷贝完成！")
