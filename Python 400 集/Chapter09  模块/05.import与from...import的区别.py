# coding:utf-8
'''
import 导入的是模块。from...import 导入的是模块中的一个函数/一个类。
如果进行类比的话，import 导入的是“文件”，我们要使用该“文件”下的内容，必
须前面加“文件名称”。from...import 导入的是文件下的“内容”，我们直接使用这
些“内容”即可，前面再也不需要加“文件名称”了。
'''
# 使用方式1
import Calculator

a = Calculator.add(30, 40)
# add(100,200) #不加模块名无法识别
print(a)

# 使用方式2
from Calculator import *

a = Calculator.add(100, 200)  # 无需模块名，可以直接引用里面的函数/类
print(a)
b = Calculator.MyNum()
b.print123()
