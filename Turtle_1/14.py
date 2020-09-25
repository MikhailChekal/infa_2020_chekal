import math
import turtle
turtle.shape('turtle')
turtle.speed(100)
turtle.tracer(0)

a = 600


def astra(number):
    if number % 2 == 1:
        for i in range(number):
            turtle.forward(a)
            turtle.left(180 - 180 / number)
    elif number % 4 == 0:
        for i in range(number):
            turtle.forward(a)
            turtle.left(180 - 360 / number)
    '''else:
        for _ in range(2):
            for i in range(number // 2):
                turtle.forward(a)
                turtle.left(180 - 360 / number)
            turtle.left(180 / number)
            turtle.penup()
            turtle.forward(a * 2 / (math.sin(math.pi / number)))
            turtle.left(180 - 180 / number)
            turtle.pendown()'''


astra(11)
turtle.tracer(1)
turtle.mainloop()