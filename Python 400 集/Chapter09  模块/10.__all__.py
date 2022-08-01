# coding:utf-8
from 包.a import module_A

module_A.func_A()  # 在这里由于已经设置好具体可以允许外部导入那些包所以
# 这里只可以使用__all__定义或者指定的有限个函数
