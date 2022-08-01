"""
try...except结构是最常见的异常处理结构，形式如下：
try:
    被监控的可能引发异常的语句块
except  BaseExcception [as e]:
    异常处理语句块

    try块包含着可能引发异常的代码，except块则用来捕捉和处理发生的异常，执行的时候，如果
    try块中没有引发异常，则跳过except块直接执行后面的代码，反之则调到except代码块处执行
    相应的异常处理，异常处理结束之后，继续执行后续的代码。
"""

# 测试遇到异常执行的顺序
# 以一个简单的0不能做除数的异常为例
try:
    print("step01")
    a = 3 / 0
    print("step02")  # 从输出结果中可以看出这句话实际上因为除零异常被捕获被跳过
except BaseException as e:
    print("step03")
    print(e)  # 输出异常对象内容
    print(type(e))  # 输出异常对象类型

print("step04")

print("--------------")
# 如果没有出现除零异常，那么就不会进入except语句块执行
try:
    print("step01")
    a = 3 / 3
    print("step02")  # 从输出结果中可以看出这句话实际上因为除零异常被捕获被跳过
except BaseException as e:
    print("step03")
    print(e)  # 输出异常对象内容
    print(type(e))  # 输出异常对象类型

print("step04")
