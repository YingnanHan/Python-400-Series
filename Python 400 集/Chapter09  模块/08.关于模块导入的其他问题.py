# coding:utf-8

'''
当导入一个模块时， 模块中的代码都会被执行。不过，如果再次导入这个模块，
则不会再次执行。
Python 的设计者为什么这么设计？因为，导入模块更多的时候需要的是定义模块
中的变量、函数、对象等。这些并不需要反复定义和执行。“只导入一次
import-only-once”就成了一种优化。
一个模块无论导入多少次，这个模块在整个解释器进程内有且仅有一个实例对象。
'''

import Test
import Test
import Test
import Test

# 如果用户确实有实际需求，想要让模块再一次被加载可以使用
import importlib

m = importlib.reload(Test)  # 这里需要使用实际的包名，而不是一个字符串
