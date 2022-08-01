# 用法一：使用traceback模块打印异常信息

# 测试traceback模块的使用

import traceback

try:
    print("test")
    num = 1 / 0
except:
    traceback.print_exc()  # 使用trackback米快下的print_exc()函数打印到控制台

# 用法二：使用traceback模块打印异常信息到日志文件
try:
    print("test")
    num = 1 / 0
except:
    with open("log.txt", "a+") as f:
        # 在传递参数f之后，使用trackback米快下的print_exc()函数打印到日志文件
        traceback.print_exc(file=f)
