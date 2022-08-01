import turtle  # 导入turtle模块

turtle.showturtle()  # 显示绘制箭头
turtle.write("Hello World")  # 书写文字
turtle.forward(300)  # 前进300单元
turtle.left(90)  # 左转90°
turtle.color("red")  # 设置画笔颜色为红色
turtle.forward(300)  # 前进300单元

turtle.goto(0, 50)  # 讲画笔移动到（0,50）同时在沿线上画出轨迹
turtle.goto(0, 0)  # 回到原点，并画出轨迹

turtle.penup()  # 抬起笔，移动时不会画出轨迹
turtle.goto(0, 300)  # 讲画笔移动到（0,300）
turtle.goto(0, 0)  # 将画笔移动到原点
turtle.pendown()  # 放下画笔
turtle.goto(0, 50)  # 移动并且绘制轨迹
turtle.goto(50, 50)

turtle.circle(100)  # 从当前位置向左绘制半径为100单位的圆

turtle.done()
