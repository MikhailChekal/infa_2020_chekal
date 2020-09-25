import turtle

turtle.shape('turtle')
turtle.speed(100)
n = 12
for i in range(1, n + 1):
    turtle.forward(100)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(100)
    turtle.right(180 - 360 / n)
turtle.mainloop()