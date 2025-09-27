import turtle #importing library
window = turtle.Screen()
window.bgcolor("light blue") #screen background color
window.title("Turtle square")
pen = turtle.Turtle()
for i in range(2):
    pen.forward(100)
    pen.left(90)

window.exitonclick()