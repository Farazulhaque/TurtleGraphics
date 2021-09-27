import turtle
pen = turtle.Turtle()
pen.hideturtle()

choice = input(
    "Enter C to see an inscribed circle\nOr T to see touching circle: ")
if choice.upper() == "C":
    size = int(input("Enter size of the square: "))
    pen.color("pink")
    pen.begin_fill()
    for i in range(4):
        pen.forward(size)
        pen.left(90)
    pen.end_fill()
    pen.forward(size/2)
    pen.color("blue")
    pen.begin_fill()
    pen.circle(size/2)
    pen.end_fill()

else:
    radius = int(input("Enter radius of the circle: "))
    pen.color("red")
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()
    pen.color("orange")
    pen.right(180)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

turtle.done()
