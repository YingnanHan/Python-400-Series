# 测试@property的用法

class Employee:

    # 将下面这个简单函数当做属性来操作，使用@property装饰器
    @property
    def salary(self):
        print("function salary is running...")
        return 10000


e = Employee()
e.salary
# 值得注意的是使用property将某一个类内部的对象设置为属性之后一般不可以修改
