"""
单例模式（Singleton Pattern）的核心作用是确保一个类只有一个实例，并且提供一
个访问该实例的全局访问点。
单例模式只生成一个实例对象，减少了对系统资源的开销。当一个对象的产生需要比较
多的资源，如读取配置文件、产生其他依赖对象时，可以产生一个“单例对象”，然后永久
驻留内存中，从而极大的降低开销。
单例模式有多种实现的方式，我们这里推荐重写__new__()的方法
"""


class MySingleton:
    # 用于保存单例对象
    __obj = None
    __init__flag = True

    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:  # 如果__obj为空，那么这次建立的对象是第一个对象
            cls.__obj = object.__new__(cls)  # 调用父类的对象创建器创建一个新的对象

        return cls.__obj  # 返回所创建的对象

    def __init__(self, name):  # 保证初始化函数__init__()仅仅被调用一次
        if MySingleton.__init__flag == True:
            print("init...")
            self.name = name
            MySingleton.__init__flag = False
        else:
            return


a = MySingleton("aa")
b = MySingleton("bb")
print(a)
print(b)
