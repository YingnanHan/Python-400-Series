'''
    map(func, *iterables) --> map object

    Make an iterator that computes the function using arguments from
    each of the iterables.  Stops when the shortest iterable is exhausted.
'''

a = 10
#将10转化为字符串
s = str(a)
print(type(s))
a = [1,2,3,4,5,6,7,8,9]#需求，将列表中的每一个元素转化为字符串
L = map(str,a)
L = list(L)
print(L)