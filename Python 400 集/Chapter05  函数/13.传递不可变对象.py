# 传递不可变对象，如果正确发生参数传递，那么参数在传递过程中发生了浅拷贝行为


# a = 10
# print("a:",id(a))
#
# def test(m):
#     print("m:",id(m))
#     m  = 20
#     print(m)
#     print("m:",id(m))
#
# test(a)


# 传递不可变对象，不可变对象里面包含的子对象是可变的话则方法中修改了这个可变对象，那么原来的
# 实际参数也会被修改
a = (10, 20, [1, 2])
print("a:", id(a))


def test(m):
    print("m:", id(m))
    # m[0]  = 20#不可以修改不可变对象
    m[2][0] = 20l
    print(m)
    print("m:", id(m))


test(a)
