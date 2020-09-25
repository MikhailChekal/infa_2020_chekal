import math
import turtle
turtle.tracer(0)

turtle.shape('turtle')
turtle.speed(100)
delta_phi = 5 / (2 * math.pi)
for i in range(1, 10000):
    turtle.left(delta_phi)
    turtle.forward(0.001 * delta_phi * math.sqrt(1 + (delta_phi * i) ** 2))

turtle.tracer(1)
turtle.mainloop()
