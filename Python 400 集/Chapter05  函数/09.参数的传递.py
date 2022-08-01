# 测试参数的传递
# 传递可变对象

a = [10, 20]

print(id(a))
print(a)
print("--------------")


def test(m):
    print(id(m))  # m实际上是对实参啊的一个引用
    m.append(300)  # 对象会被修改
    print(id(m))


test(a)
print(a)  # 此时源对象已发生改变
