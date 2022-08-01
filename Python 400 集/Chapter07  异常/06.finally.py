# finally结构中，无论是否发生异常都会执行finally语句块，通常被用来释放try中
# 申请的资源，，比如文件句柄

try:
    a = input("请输入一个被除数：")
    b = input("请输入一个除数：")
    c = float(a) / float(b)
except BaseException as e:
    print(e)
else:
    print(c)
finally:
    print("无论异常是否发生，finally语句块的内容都会被执行")
print("程序结束！！！")
