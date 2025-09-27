import turtle #importing library
my= turtle.Screen()
my.bgcolor("light blue") #screen background color
my.title("Turtle")
pen = turtle.Turtle()
size=0
while True:
    for i in range(4):
        pen.forward(size+1)
        pen.left(90)