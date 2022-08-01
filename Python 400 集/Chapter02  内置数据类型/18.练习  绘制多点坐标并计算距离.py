import turtle

# 定义多个点的坐标
x1, y1 = 100, 100
x2, y2 = 100, -100
x3, y3 = -100, -100
x4, y4 = -100, 100

# 绘制折线
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.goto(x1, y1)
turtle.goto(x2, y2)
turtle.goto(x3, y3)
turtle.goto(x4, y4)

# 计算起始点与终点之间的位移
import math

l = math.sqrt((x1 - x4) ** 2 + (y1 - y4) ** 2)
turtle.write(l)
turtle.done()
