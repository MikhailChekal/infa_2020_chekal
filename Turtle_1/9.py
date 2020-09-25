import turtle
import math

turtle.shape('turtle')
turtle.speed(5)
len = 100


def polygon(number, len):
    n = number + 3
    length = len
    a = 180 - 180 * (n - 2) / n
    for j in range(n):
        turtle.left(a)
        turtle.forward(length)
    turtle.right(-a / 2 + 90)
    length /= (math.cos(math.pi / (n + 1)))
    turtle.penup()
    turtle.goto(-50, 28.86)
    turtle.forward(length / 2 * (1 / math.sin(math.pi / (n + 1))))
    turtle.left(90 * (n - 1) / (n + 1))
    turtle.pendown()
    return length


for i in range(10):
    len = polygon(i, len)
turtle.mainloop()