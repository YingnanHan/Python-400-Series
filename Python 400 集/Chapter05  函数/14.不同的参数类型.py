# 测试 传递参数的类型 ：位置参数 默认值参数 命名参数

def test01(a, b, c, d):
    print("{0}-{1}-{2}-{3}".format(a, b, c, d))


def tets02(a, b, c=10, d=20):  # 定义默认值参数的时候，默认值参数必须放在位置参数的后面
    print("{0}-{1}-{2}-{3}".format(a, b, c, d))


test01(1, 2, 3, 4)  # 使用位置参数
# test01(1,2,3)   #如果在使用位置参数的过程中，发生参数不匹配的情况，会抛出TypeError异常

test01(d=20, b=10, a=10, c=100)  # 使用命名参数，通过形参名字来传递参数

tets02(2, 3)
tets02(2, 3, 4)
