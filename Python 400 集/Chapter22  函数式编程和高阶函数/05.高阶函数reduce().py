from functools import reduce

'''
reduce(function, sequence[, initial]) -> value

    Apply a function of two arguments cumulatively to the items of a sequence,
    from left to right, so as to reduce the sequence to a single value.
    For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the sequence in the calculation, and serves as a default when the
    sequence is empty.
'''
#对如下列表内部元素求和
res = reduce(lambda a,b:a+b ,[1,2,3,4,5,6,7,8,9,10])#第一个参数是lambda表达式，第二个参数是列表
print(res)

#将列表里面的元素拼接成一个更大的整数
res = reduce(lambda a,b:a*10+b ,[1,2,3,4,5,6,7,8,9,10])#第一个参数是lambda表达式，第二个参数是列表
print(res)