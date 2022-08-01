def foo():
    print('starting')
    while True:
       res= yield 4
       print('res:',res)

'''
在函数中使用了yield，则该函数就称为了一个生成器
yield的理解
1.当成return  程序返回
2.当成生成器
'''
g=foo()  #g就是一个生成器对象
print(type(g))
print(next(g))
print('*'*20)
print(next(g))