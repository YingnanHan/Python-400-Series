def foo():
    print('starting')
    while True:
        res = yield 4
        print('res:',res)

g = foo()
print(next(g))
# print(next(g))
print(g.send(10))