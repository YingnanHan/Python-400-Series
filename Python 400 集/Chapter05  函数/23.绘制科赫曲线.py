import turtle as t  # 绘制科赫曲线


def Kole(lenth, n):
    if n == 0:
        t.fd(lenth)
    else:
        for i in [0, 60, -120, 60]:
            t.left(i)
            Kole(1 / 3 * lenth, n - 1)


def main():  # 绘制科赫雪花
    t.setup(800, 600)
    t.hideturtle()
    t.pensize(5)
    t.pencolor("green")
    t.pu()
    t.goto(-300, 0)
    t.pd()
    lenth = 200
    n = 3
    for i in range(3):
        Kole(lenth, n)
        t.left(-120)


main()
t.done()
