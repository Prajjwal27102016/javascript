import turtle #importing library
pen=turtle.Turtle()
pen.pensize(5)
pen.shape("turtle")
for i in range(4):
    pen.forward(100)
    pen.left(90)
turtle.done()
turtle.exitonclick()