import turtle
myTurtle = turtle.Turtle()
myTurtle.width(2)
myTurtle.hideturtle()


# used for drawing squares
def drawSquare(myTurtle, sideLength):
    for i in range(4):
        myTurtle.forward(sideLength)
        myTurtle.right(90)


# used for calling function drawSquare
def myturtle():
    myTurtle.left(45)

    sideLength = 100
    for i in range(4):
        drawSquare(myTurtle, sideLength)
        sideLength -= 25

    myTurtle.right(180)

    sideLength = 100
    for i in range(4):
        drawSquare(myTurtle, sideLength)
        sideLength -= 25


myturtle()

turtle.done()
