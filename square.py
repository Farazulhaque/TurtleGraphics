import turtle
t = turtle.Turtle()


def drawSquare(myTurtle, sideLength):
    # loop 4 times to create 2, 3, 4 sides
    for i in range(4):
        myTurtle.forward(sideLength)
        myTurtle.right(90)  # side 1


drawSquare(t, 80)

turtle.done()

