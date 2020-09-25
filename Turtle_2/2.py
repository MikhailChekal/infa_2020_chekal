import turtle
import math

reductor = 0.5
numbers = []
with open('number.txt', 'r') as file:
    for line in file:
        N = line
#N = '141700'#input()
for i in range(len(N)):
    numbers.append(int(N[i]))
print(numbers)


number_0 = (0, -90, 100, 90, 50, 90, 100, 90, 50)
number_1 = (50, -90, 100, -135, 50 * math.sqrt(2))
number_2 = (50, -180, 50, 135, 50 * math.sqrt(2), -45, 50, -90, 50)
number_3 = (0, -45, 50 * math.sqrt(2), -135, 50, 135, 50 * math.sqrt(2), -135, 50)
number_4 = (50, -90, 100, 180, 50, 90, 50, 90, 50)
number_5 = (0, 0, 50, -90, 50, -90, 50, 90, 50, 90, 50)
number_6 = (0, 0, 50, -90, 50, -90, 50, 90, 50, 90, 50, 180, 50, -90, 100)
number_7 = (0, -90, 50, 45, 50 * math.sqrt(2), -135, 50)
number_8 = (0, 0, 50, -90, 100, -90, 50, -90, 100, 180, 50, 90, 50)
number_9 = (0, -45, 50 * math.sqrt(2), -45, 50, -90, 50, -90, 50, -90, 50)

spisok = [number_0, number_1, number_2, number_3, number_4, number_5, number_6, number_7, number_8, number_9]

Numbers = []
for i in range(len(numbers)):
    Numbers.append(spisok[numbers[i]])

for t in range(len(Numbers)):
    j = 0
    turtle.penup()
    turtle.forward(reductor * Numbers[t][0])
    turtle.pendown()
    while j < len(Numbers[t]) - 1:
        j += 1
        turtle.right(Numbers[t][j])
        j += 1
        turtle.forward(reductor * Numbers[t][j])

    turtle.penup()
    turtle.goto(reductor * ((t + 1) * 75), 0)
    turtle.setheading(0)
    turtle.pendown()

turtle.mainloop()
