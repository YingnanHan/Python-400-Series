"""
基本的文本文件写入操作：
    文本文件的写入一般就是三个步骤：
        1.创建文件对象
        2.写入数据
        3.关闭文件对象
"""

f = open("file/a.txt", "a")  # 以追加的模式打开文件a.txt如果没有改文件，则创建
f.write("hello world!")
f.close()
