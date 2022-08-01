# python中实际上是没有重载的，定义多个同名函数，实际上只有最后一个有效

class Person:

    def say_hi(self):
        print("hello")

    def say_hi(self, name):
        print("hi {0}".format(name))


p = Person()
# p.say_hi()#这样的写法是错误的，实际上这个时候之前的say_hi已经被覆盖掉了
p.say_hi("Mike")
