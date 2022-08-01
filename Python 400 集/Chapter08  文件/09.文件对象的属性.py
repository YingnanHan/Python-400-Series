# coding=utf-8
with open("file/f.txt", "r", encoding="utf-8") as f:
    print("文件名是{0}".format(f.name))
    print(f.tell())  # 输出当前文件指针的位置
    print("读取的内容{0}".format(str(f.readline())))  # 读取第一行
    f.seek(10)  # 找到文件的第10个字节的位置
    '''
    fileObject.seek(offset, [whence])
    offset -- 开始的偏移量，也就是代表需要移动偏移的字节数，如果是负数表示从倒数第几位开始。
    whence：可选，默认值为 0。给 offset 定义一个参数，表示要从哪个位置开始偏移；0 代表从文件开头开始算起，1 代表从当前位置开始算起，2 代表从文件末尾算起。
    '''
    print(f.tell())  # 输出当前文件指针的位置从0开始
    print("读取的内容{0}".format(str(f.readline())))  # 继续从当前指针所指位置后开始读取文件
