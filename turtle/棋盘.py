#画棋盘
import turtle

width = 30
num = 18

x1 = [(-400, 400), (-400 + width * num, 400)]
y1 = [(-400, 400), (-400, 400 - width * num)]
t = turtle.Pen()
t.speed(10)

for i in range(0, 19):
    t.penup()
    t.goto(x1[0][0], x1[0][1] - 30 * i)
    t.pendown()
    t.goto(x1[1][0], x1[1][1] - 30 * i)

for i in range(0, 19):
    t.penup()
    t.goto(y1[0][0] + 30 * i, y1[0][1])
    t.pendown()
    t.goto(y1[1][0] + 30 * i, y1[1][1])

t.hideturtle()  # 隐藏画笔
turtle.done()  # 保证运行窗口不被自动关闭
