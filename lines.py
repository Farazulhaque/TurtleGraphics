import turtle

pen = turtle.Turtle()
pen.speed(0)

# To count number of clicks
count = 0
# To count number of lines
line = 0


def drawLine(x, y):
    # Here x and y are co-ordinates of mouse click
    global count, line
    # Increment count varible by 1 on every click
    count += 1
    # To draw only 5 lines check line == 5
    if line == 5:
        pen.hideturtle()
        turtle.done()
    # To check if it is odd click
    if count % 2 != 0:
        # Pen up and go to x, y co-ordinates
        pen.up()
        pen.goto(x, y)
    else:
        # Pen down and go to x, y co-ordinates
        pen.down()
        pen.goto(x, y)
        # Increment line by 1
        line += 1


# Call function drawLine to draw a line
turtle.onscreenclick(drawLine)
turtle.done()
