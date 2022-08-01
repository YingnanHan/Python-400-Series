#总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），
#返回一个新的函数，调用这个新函数会更简单。

#①
# print(int("12345",base=8))
# print(int("12345",base=16))
# #将10101010转化为十进制整数
# print(int("101010101011110",base=2))


#定义函数
def new_int(s,base=2):
    return int(s,base=base)
print(new_int("10101010"))

#偏函数就是将上面的函数进行简化的功能也就是将函数的某一些参数固定
from functools import partial
new_int = partial(int,base=2)
print(new_int("10101010"))#在这里实际上偏函数为用户定义了一个满足用户需求的新函数