import turtle

turtle.shape('turtle')
turtle.speed(10)


def circle(number):
    for i in range(36):
        turtle.forward(10 + number * 2)
        turtle.left(10)
    for i in range(36):
        turtle.forward(10 + number * 2)
        turtle.right(10)


n = 6
turtle.right(90)
for j in range(n):
    circle(j)
turtle.mainloop()