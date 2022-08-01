'''
    map(func, *iterables) --> map object

    Make an iterator that computes the function using arguments from
    each of the iterables.  Stops when the shortest iterable is exhausted.
'''

a = [1,2,3,4]
b = [10,20,30,40]

#自定义需要被调用的函数
def func(a,b):
    return a+b

#如果需要操作多个可迭代对象，那么只需要按照顺序排列下来
#res = list(map(func,a,b))#如果a,b长度不一致，那么就按照长度较小的那个列表的长度作为迭代的次数
res = list(map(lambda a,b:a+b,a,b))
print(res)