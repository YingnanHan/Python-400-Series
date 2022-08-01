# 造成除零异常  ZeroDivisionError: division by zero
# 方式一
# a = 1 / 0

"""
F:\Anaconda\python.exe "H:/Python 400 集/Chapter07  异常/01.测试异常.py"           文件名称，表示哪一个位置的文件出现异常
Traceback (most recent call last):                                                追溯异常位置
  File "H:/Python 400 集/Chapter07  异常/01.测试异常.py", line 2, in <module>       指出发出异常的位置，行号
    a = 1 / 0                                                                     给出异常出现位置附近的代码
ZeroDivisionError: division by zero                                               给出异常的类型

Process finished with exit code 1                                                 程序/进程退出码

"""


# 方式二，   一般来讲如果因为异常是由于某一个被调用的函数导致，可能会出现多个位置出现异常的假象
#          解决办法一般是将一大串异常信息从下往上看，顺次检查各个位置
#          举例如下

def a():
    num = 1 / 0


def b():
    a()


def c():
    b()


c()

'''
Traceback (most recent call last):
  File "H:/Python 400 集/Chapter07  异常/01.测试异常.py", line 29, in <module>
    c()
  File "H:/Python 400 集/Chapter07  异常/01.测试异常.py", line 27, in c
    b()
  File "H:/Python 400 集/Chapter07  异常/01.测试异常.py", line 24, in b
    a()
  File "H:/Python 400 集/Chapter07  异常/01.测试异常.py", line 21, in a
    num = 1/0
ZeroDivisionError: division by zero
遇到这种情况应当从21行开始看哪里发生了除零错误
'''
