# coding=utf-8
# writelines()函数将字符串列表直接写入到文件中

f = open("file/c.txt", "w")
l = ["abc", '\n', "def", '\n', "ghi"]
f.writelines(l)
f.close()
