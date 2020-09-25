import turtle

turtle.shape('turtle')
turtle.speed(10)
turtle.left(180)


def circle(number):
    if number % 2 == 0:
        for i in range(18):
            turtle.forward(10)
            turtle.right(10)
    else:
        for i in range(18):
            turtle.forward(2)
            turtle.right(10)


n = 10
turtle.right(90)
for j in range(n):
    circle(j)
turtle.mainloop()
