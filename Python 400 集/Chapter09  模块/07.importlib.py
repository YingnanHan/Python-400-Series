# coding:utf-8
'''
一般不建议我们自行使用__import__()导入，其行为在 python2 和 python3 中
有差异，会导致意外错误。如果需要动态导入可以使用 importlib 模块
'''

import importlib

obj = importlib.import_module("math")  # 如果只穿一个参数，那么只传入包名
res = obj.sin(100)  # 弧度制
print(res)
