import turtle

turtle.shape('turtle')
for i in range(100):
    turtle.forward(20 + 10 * i)
    turtle.left(90)
turtle.mainloop()