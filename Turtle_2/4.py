import math
import random as rd
import turtle


a = 300
turtle.tracer(0)
turtle.penup()
turtle.goto(-a, -a)
turtle.pendown()
turtle.goto(a, -a)
turtle.goto(a, a)
turtle.goto(-a, a)
turtle.goto(-a, -a)
turtle.tracer(1)

molecules_number = 3
time = 1

pool = [turtle.Turtle(shape='circle') for i in range(molecules_number)]
for molecule in pool:
    molecule.penup()
    molecule.speed(50)
    x = rd.randint(-100, 100)
    y = rd.randint(-100, 100)
    molecule.goto(x, y)
    molecule.left(rd.random() * 360)
time_distance = []
molecule_distance = []
dist = []
for i in range(time):
    for molecule in pool:
        molecule.color('green')
        molecule.pendown()
        molecule.forward(5)
        if molecule.pos()[1] > a and 0 <= molecule.heading() <= 90:
            molecule.right(2 * molecule.heading())
        if molecule.pos()[1] > a and 180 >= molecule.heading() > 90:
            molecule.left(2 * (180 - molecule.heading()))

        if molecule.pos()[1] < -a and 180 <= molecule.heading() <= 270:
            molecule.right(2 * (-180 + molecule.heading()))
        if molecule.pos()[1] < -a and 360 > molecule.heading() > 270:
            molecule.left(2 * (360 - molecule.heading()))
 ##################################################################################
        if molecule.pos()[0] < -a and 90 < molecule.heading() <= 180:
            molecule.right(2 * (-90 + molecule.heading()))
        if molecule.pos()[0] < -a and 270 >= molecule.heading() > 180:
            molecule.left(2 * (270 - molecule.heading()))

        if molecule.pos()[0] >=a and 360 > molecule.heading() >= 270:
            molecule.right(2 * (molecule.heading() - 270))
        if molecule.pos()[0] > a and 0 < molecule.heading() <= 90:
            molecule.left(2 * molecule.heading())

for k in range(time):
    for molecule in pool:
        for i in range(len(pool)):
        #for molecule in pool:
            dist.append(molecule.distance(pool[i]))
            #dist.append(molecule.distance(molecule))
        molecule_distance.append(dist)
    time_distance.append(molecule_distance)
print(time_distance)
