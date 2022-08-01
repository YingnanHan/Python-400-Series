# 例子：循环输入数字，如果不是数字则处理异常，如果输入88，则结束循环

while True:
    try:
        x = int(input("请输入一个数字："))
        print("输入的数字：", x)
        if x == 88:
            print("退出程序")
            break
    except ValueError as e:
        print(e)
        print("异常，输入内容不是一个数字")

print("循环输入数字程序结束")
