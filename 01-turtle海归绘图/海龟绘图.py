import turtle #导入turtle模块
turtle.showturtle() #显示箭头
turtle.write("高淇") #写字符串
turtle.forward(300) #前进300像素
turtle.color("red") #画笔颜色改为red
turtle.left(90) #箭头左转90度
turtle.forward(300)
turtle.goto(0,50) #去坐标（0,50）
turtle.goto(0,0)
turtle.penup() #抬笔。这样，路径就不会画出来
turtle.goto(0,300)
turtle.pendown() #下笔。这样，路径就会画出来
turtle.circle(100) #画圆
