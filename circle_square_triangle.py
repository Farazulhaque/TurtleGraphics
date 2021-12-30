import turtle

# variables
pen_color = str()
fill_color = str()
pen_size = int()

# Moving the pen
turtle.penup()
turtle.goto(0, 150)
turtle.pendown()
turtle.left(180)

pen_size = int(input("Enter Pen size (1-10): "))
pen_color = input("Enter pencolor(red, blue or yellow): ").lower()
if pen_color == "red":
    fill_color = "yellow"
elif pen_color == "blue":
    fill_color = "red"
else:
    fill_color = "green"
turtle.pensize(pen_size)
turtle.pencolor(pen_color)
turtle.fillcolor(fill_color)


turtle.begin_fill()
# draw circle
turtle.circle(50)
# stopping the fill
turtle.end_fill()

turtle.penup()
turtle.left(90)
turtle.forward(150)
turtle.pendown()

pen_color = input("Enter pencolor(red, blue or yellow): ").lower()
if pen_color == "red":
    fill_color = "yellow"
elif pen_color == "blue":
    fill_color = "red"
else:
    fill_color = "green"

turtle.pencolor(pen_color)
turtle.fillcolor(fill_color)

turtle.begin_fill()
# drawing a square
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.end_fill()

turtle.penup()
turtle.left(90)
turtle.forward(150)
turtle.pendown()

pen_color = input("Enter pencolor(red, blue or yellow): ").lower()
if pen_color == "red":
    fill_color = "yellow"
elif pen_color == "blue":
    fill_color = "red"
else:
    fill_color = "green"

turtle.pencolor(pen_color)
turtle.fillcolor(fill_color)

turtle.begin_fill()
# drawing a triangle
turtle.right(35)
turtle.forward(125)
turtle.right(235)
turtle.forward(150)
turtle.left(127)
turtle.forward(130)
turtle.end_fill()

turtle.mainloop()
