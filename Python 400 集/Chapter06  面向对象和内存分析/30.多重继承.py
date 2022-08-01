class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def string(self):
        print("X:{0},Y:{1}".format(self.x, self.y))


# class Circle(Point):
#
#     def __init__(self,x,y,radius):
#         super().__init__(x,y)
#         self.radius = radius
#
#     def string(self):
#         print("该图形初始化点为:({0},{1}),半径为:{2}。".format(self.x,self.y,self.radius))


class Size:

    def __init__(self, width, heigth):
        self.width = width
        self.height = heigth

    def string(self):
        print("Width:{0},Height:{1}".format(self.width, self.height))


class Rectangle(Point, Size):

    def __init__(self, x, y, width, height):
        super(Rectangle, self).__init__(x, y)
        super(Point, self).__init__(width, height)
        # 这里值得注意的是，如果要跨过一个父类去另外一个父类调用同名方法时
        # 应当在super()的参数中指定要继承的类在继承顺序中的前一个类的名称
        # 如果没有就把这个名称写成自己的类名

    def string(self):
        print("该图形的初始化点为({0},{1}),长宽分别为Height:{2},Width:{3}".format(self.x, self.y, self.height, self.width))


if __name__ == '__main__':
    # c = Circle(0,0,100)
    # c.string()

    r = Rectangle(0, 0, 100, 100)
    r.string()
