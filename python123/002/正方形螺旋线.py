import turtle
n=10
for i in range(1,10,1):
    for j in [90,180,-90,0]:
        turtle.seth(j)
        turtle.fd(n)
        n+=5
turtle.hideturtle()
turtle.done()