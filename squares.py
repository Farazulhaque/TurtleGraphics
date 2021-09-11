import turtle

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.up()
pen.goto(-250, 250)
pen.down()
n = int(input("Please enter the numner of sub-divisions: "))
for i in range(4):
    for i in range(n):
        pen.width(2)
        pen.forward(40)
        pen.width(1)
        if i != n-1:
            pen.right(90)
            pen.forward(10)
            pen.right(180)
            pen.forward(10)
            pen.right(90)
    pen.right(90)


# pen.right(180)
pen.forward(40)
pen.right(90)
for j in range(n-1):
    for i in range(n):
        pen.up()
        pen.forward(30)
        pen.down()
        if i != n-1:
            pen.forward(20)
            pen.right(180)
            pen.forward(10)
            pen.right(90)
            pen.forward(10)
            pen.right(180)
            pen.forward(20)
            pen.right(180)
            pen.forward(10)
            pen.circle(1)
            pen.right(90)
            pen.circle(1)
            pen.right(90)
            pen.circle(1)
            pen.left(90)
            # pen.right(90)
            pen.forward(10)
            pen.backward(10)
        else:
            pen.forward(10)
            if j % 2 != 0:
                pen.right(90)
                pen.forward(40)
                pen.right(90)
            else:
                pen.left(90)
                pen.forward(40)
                pen.left(90)


turtle.done()
