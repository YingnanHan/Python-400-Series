# coding:utf-8

'''
import 语句本质上就是调用内置函数__import__()，我们可以通过它实现动态导入。给
__import__()动态传递不同的的参数值，就能导入不同的模块。
注意：一般不建议我们自行使用__import__()导入，其行为在 python2 和 python3 中
有差异，会导致意外错误。如果需要动态导入可以使用 importlib 模块
'''

import math

print(math.sin(10))

# 等价于
m = __import__("math")

print(m.sin(10))
