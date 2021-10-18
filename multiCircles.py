import turtle
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.width(2)


colors = ['red', 'blue', 'orange', 'brown', 'magenta']

# initial radius
radius = 20

# set position
x = 0
y = 0
pen.up()
pen.goto(x, y)
pen.down()

# print 20 circles
# increment radius to 10 on each iteration
for i in range(20):
    if i in range(5):
        col = colors[0]
    elif i in range(5, 10):
        col = colors[1]
    elif i in range(10, 15):
        col = colors[2]
    elif i in range(15, 20):
        col = colors[3]

    # change color of pen
    pen.color(col)
    # draw circle
    pen.circle(radius)
    radius += 10

    # to change position of turtle
    y -= 10
    pen.up()
    pen.goto(x, y)
    pen.down()

turtle.done()
