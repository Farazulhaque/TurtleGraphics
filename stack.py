import turtle


def main():
    # Moving the pen
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()

    for i in range(7):
        if i % 2 == 0:
            turtle.penup()
            turtle.backward(25)
            turtle.pendown()
            drawSquare()
        else:
            turtle.penup()
            turtle.forward(25)
            turtle.pendown()
            drawCircle()
        turtle.penup()
        turtle.left(90)
        turtle.forward(60)
        turtle.right(90)
        turtle.pendown()


def drawSquare():
    for i in range(4):
        turtle.forward(50)
        turtle.left(90)


def drawCircle():
    turtle.circle(50/2)


main()
turtle.mainloop()
