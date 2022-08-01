# coding:utf-8

#使用包内函数的方式①
import 包.a.aa.module_AA #导入包的时候必须要从最顶端的包开始写路径
包.a.aa.module_AA.fun_AA()

#使用包内函数的方式②
from 包.a.aa import module_AA
module_AA.fun_AA()

#使用包内函数的方式③
from 包.a.aa.module_AA import fun_AA #直接导入特定的函数
fun_AA()

