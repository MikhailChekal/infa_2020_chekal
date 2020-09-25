import turtle

turtle.tracer(0)
turtle.goto(1000,0)
turtle.goto(-400,0)
turtle.tracer(1)

x = -400
y = 0
Vx = 20
Vy = 30
ay = -10


for t in range(1000):
    dt = 0.1
    t += dt

    x += Vx * dt
    y += Vy * dt + ay * dt ** 2 / 2
    Vy += ay * dt

    turtle.goto(x, y)
    if y <= 0:
        Vy = -Vy
