import math
import turtle
turtle.speed(10)
turtle.shape('turtle')
for j in range(10):
    for i in range(4):
        turtle.left(90)
        turtle.forward(200 + 40 * j)
    turtle.right(45)
    turtle.penup()
    turtle.forward(math.sqrt(2) * 20)
    turtle.left(45)
    turtle.pendown()
turtle.mainloop()