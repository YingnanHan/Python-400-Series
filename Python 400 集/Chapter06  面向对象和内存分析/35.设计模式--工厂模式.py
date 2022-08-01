"""
    设计模式是面向对象语言特有的内容，是我们在面临某一类问题时候固定的做法，设计
模式有很多种，比较流行的是：GOF（Goup Of Four）23 种设计模式。
    工厂模式实现了创建者和调用者的分离，使用专门的工厂类将选择实现类、创建对象进
行统一的管理和控制
"""


class CarFactory:

    # 所谓的"造车工厂"
    def createCar(self, brand):
        """
        用于创造车的对象
        :return:
        """
        if brand == "奔驰":
            return Benz()
        if brand == "宝马":
            return BMW()
        if brand == "比亚迪":
            return BYD()
        else:
            return "未知品牌，无法创建"


class Benz:

    def __str__(self):
        return "Benz"


class BMW:

    def __str__(self):
        return "BMW"


class BYD:

    def __str__(self):
        return "BYD"


# 调用的时候"先建工厂"
factory = CarFactory()
c1 = factory.createCar("奔驰")
c2 = factory.createCar("比亚迪")
print(c1)
print(c2)
