import turtle

t = turtle.Pen()
t.speed(4)
t.width(4)

my_colors = ("red", "green", "yellow", "black")

for i in range(50):
    t.penup()
    t.goto(0, -i * 10)
    t.pendown()
    t.circle(15 + i * 10)
    t.color(my_colors[i % 4])

t.done()
