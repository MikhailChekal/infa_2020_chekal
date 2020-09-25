import turtle
turtle.tracer(0)

turtle.shape('turtle')
turtle.speed(10)


def circle(number, color):
    turtle.begin_fill()
    for i in range(35):
        turtle.right(10.3)
        turtle.forward(number * 2)
    if color == 1:
        turtle.color('yellow')
    elif color == 2:
        turtle.color('blue')
    turtle.end_fill()
    turtle.color('black')


def semicircle(number):
    turtle.color('red')
    for i in range(17):
        turtle.left(10)
        turtle.forward(number * 2)


turtle.left(5.15)
turtle.goto(0, 0)

circle(10, 1)

turtle.penup()
turtle.goto(-50, -50)
turtle.pendown()

circle(1, 2)

turtle.penup()
turtle.goto(50, -50)
turtle.pendown()

circle(1, 2)

turtle.penup()
turtle.goto(0, -100)
turtle.pendown()

turtle.width(5)
turtle.color('red')
turtle.goto(0, -120)
turtle.color('black')

turtle.penup()
turtle.goto(-50, -120)
turtle.right(90)
turtle.pendown()
semicircle(4)

turtle.tracer(1)
turtle.mainloop()