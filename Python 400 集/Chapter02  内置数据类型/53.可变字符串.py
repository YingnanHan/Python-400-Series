import io

s = "hello world!"

sIO = io.StringIO(s)  # 生成一个可变字符串对象
print(sIO)  # 打印可变字符串对象的地址
print(sIO.read())  # 读取可变字符串中的内容
print(sIO.getvalue())  # 功能同上
sIO.seek(6)
sIO.write("China!")
print(sIO.getvalue())
