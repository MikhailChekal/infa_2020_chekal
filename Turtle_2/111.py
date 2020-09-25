import math
import random as rd
import turtle

turtle.tracer(0)
turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()
turtle.goto(200, -200)
turtle.goto(200, 200)
turtle.goto(-200, 200)
turtle.goto(-200, -200)
turtle.tracer(1)

turtle.penup()
molecules_number = 10
time = 1000
x = 0
y = 0
vx = 0.1
vy = 0.3
turtle.goto(x, y)
turtle.right(74)
for t in range(1000):
    place = [vx * t + x, vy * t + y]
    turtle.goto(place[0], place[1])
    if turtle.pos()[0] >= 200 or turtle.pos()[0] <= -200:
        vx = -vx
    if turtle.pos()[1] >= 200 or turtle.pos()[1] <= -200:
        vy = -vy