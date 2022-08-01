# coding:utf-8
'''
import 语句的基本语法格式如下：
    import 模块名 #导入一个模块
    import 模块 1，模块 2… #导入多个模块
    import 模块名 as 模块别名 #导入模块并使用新名字
import 加载的模块分为四个通用类别：
    a.使用 python 编写的代码（.py 文件）；
    b.已被编译为共享库或 DLL 的 C 或 C++扩展；
    c.包好一组模块的包
    d.使用 C 编写并链接到 python 解释器的内置模块；
        我们一般通过 import 语句实现模块的导入和使用，import 本质上是使用了内置函数
        __import__()。
当我们通过 import 导入一个模块时，python 解释器进行执行，最终会生成一个对象，
这个对象就代表了被加载的模块。
'''

import math

print(id(math))
print(type(math))
print(math.pi)  # 通过 math.成员名来访问模块中的成员

'''
由上，我们可以看到 math 模块被加载后，实际会生成一个 module 类的对象，该对象被
math 变量引用。我们可以通过 math 变量引用模块中所有的内容。
我们通过 import 导入多个模块，本质上也是生成多个 module 类的对象而已。
有时候，我们也需要给模块起个别名，本质上，这个别名仅仅是新创建一个变量引用加
载的模块对象而已
'''

# 于是，上面的代码可以按照如下方式编写
import math as m

print(id(m))
print(type(m))
print(m.pi)  # 通过 math.成员名来访问模块中的成员
