'''
    map(func, *iterables) --> map object

    Make an iterator that computes the function using arguments from
    each of the iterables.  Stops when the shortest iterable is exhausted.
'''
# an simple example of the application of function map

#定义一个函数f(x)=x²，将其作用在某一个列表中,最终得到一个新的列表

#A.传统做法
# l = [1,2,3,4,5,6,7,8]
# def f(x):
#     return x*x
# res = []
# for i in l:
#     res.append(f(i))
# print(res)

#B.使用map实现
l = [1,2,3,4,5,6,7,8]
def f(x):
    return x*x
#返回值是一个可迭代对象
iter = map(f,l)
#对iter可迭代性的判定
from collections import Iterator
print(isinstance(iter,Iterator))
#遍历结果
print(list(iter))#将可迭代对象强制转化为列表并输出
