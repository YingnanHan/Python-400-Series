# coding=utf-8
# 结合异常机制finally确保关闭文件对象
try:
    f = open(r"file/d.txt", "a")
    str = "hello"
    f.write(str)
except BaseException as e:
    print(e)
finally:
    f.close()
