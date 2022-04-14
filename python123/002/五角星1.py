import turtle
turtle.pensize(5)
turtle.pencolor("yellow")
turtle.fillcolor("red")
turtle.begin_fill()
for i in range(5):
    turtle.fd(100)
    turtle.left(72)
    turtle.fd(100)
    turtle.right(144)
turtle.end_fill()
turtle.hideturtle()
turtle.done()