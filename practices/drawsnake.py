import turtle
turtle.setup(650,350,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()  #落下画笔，不会绘制一点
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)  #setheading方向控制 向右转40度
for i in range(4):
    turtle.circle(40,80)  #半径40, 第一象限, 左转80度
    turtle.circle(-40,80) #半径40, 第三象限, 右转80度
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()
