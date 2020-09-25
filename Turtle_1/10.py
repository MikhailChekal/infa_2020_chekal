import turtle

turtle.shape('turtle')
turtle.speed(10)


def circle():
    for i in range(36):
        turtle.forward(10)
        turtle.left(10)
    for i in range(36):
        turtle.forward(10)
        turtle.right(10)


n = 6
for j in range(n):
    circle()
    turtle.right(180 / n)
turtle.mainloop()