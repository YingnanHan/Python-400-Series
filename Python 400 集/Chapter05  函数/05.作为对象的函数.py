# 测试作为函数的对象

def test01():
    print("Hello World!")


# 将函数名字作为值相函数对象的引用赋值给c，从而c指向了test01函数对象
c = test01
c()

# 说明二者指向同一个对象
print(id(c))
print(id(test01))
