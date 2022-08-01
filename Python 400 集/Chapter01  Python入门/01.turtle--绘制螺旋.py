# 引入海龟绘图包
import turtle

# 定义一个画笔对象
t = turtle.Pen()
# 通过循环实现图像的绘制
for x in range(360):
    t.forward(x)
    t.left(62)  # 向左旋转62°
# 停止作图
t.down()
