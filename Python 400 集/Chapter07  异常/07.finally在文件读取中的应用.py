try:
    f = open("test.txt", "r")
    content = f.read()
    print(content)
except:
    print("文件不存在")
finally:
    print("文件资源关闭")
    try:
        f.close()
    except BaseException as e:
        print(e)
print("程序执行结束！")
