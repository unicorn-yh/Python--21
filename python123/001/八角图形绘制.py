#使用 turtle 库，绘制一个八角图形。
#请在横线中填写Python表达式或语句，实现所需要的功能
#注意：补充代码将以匹配方式评阅，代码中不要出现空格

'''import turtle as t
t.pensize(2)
for i in range(___________):
    t.fd(150)
    t.left(___________)'''


import turtle as t
t.pensize(2)
def octagon1():
    for i in range(8):
        t.fd(150)
        t.left(135)
def octagon2():
    t.color('purple')
    for i in range(8):
        t.fd(45)
        t.right(67.5)
        t.fd(45)
        t.left(112.5)
def octagon3():
    t.colormode(255)
    t.color(255,215,0)
    t.begin_fill()
    for i in range(8):
        t.fd(200)
        t.left(225)
    t.end_fill()
def words():
    t.pencolor("black")
    t.write('八角图形绘制   Octagon drawing',font=("Times New Roman",18,"normal"))
def main():
    octagon1()
    t.penup()
    t.backward(250)
    t.pendown()
    octagon2()
    t.penup()
    t.right(23)
    t.fd(150)
    t.pendown()
    octagon3()
    t.penup()
    t.left(135)
    t.fd(230)
    words()
    t.hideturtle()
    t.done()
main()


