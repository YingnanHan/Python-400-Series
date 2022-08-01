"""
单个except结构可以捕获所有的异常，在工作中也很常见，但是从经典理论考虑，一般建议尽量
捕获可能出现的多个异常（按照先子类后父类的顺序），并且针对性的写出异常处理代码，为了
避免遗漏可能出现的异常情况，可以在最后增加BaseException，结构如下
try
    被监控的，可能引发异常的语句块
exception Exception1：
    处理 Exception1的语句块
exception Exception2:
    处理Exception2的语句块
......
exception BaseExcception:
    处理可能遗漏的异常语句块

原则  子类在前父类在后
"""

# 测试
try:
    a = input("请输入一个被除数:")
    b = input("请输入一个除数:")
    c = float(a) / float(b)
    print(c)
except ZeroDivisionError:
    print("异常，除数不能为零")
except ValueError:
    print("异常，不能将字母直接转化为数字")
except NameError:
    print("异常，变量不存在")
except BaseException:
    print("其他异常")  # 兜底作用
