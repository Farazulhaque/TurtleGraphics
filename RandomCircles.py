import time
import random
import turtle

turtle.hideturtle()
turtle.speed(0)
turtle.width(2)

screen = turtle.Screen()
screen.setup(600, 600)

# variables
horizontal = int()
radius = int()
colors = ["red", "blue", "yellow", "green"]
pen_size = int()

horizontal = -200
radius = 25
pen_size = 2

for count in range(0, 4):
    turtle.fillcolor(colors[count])
    turtle.pensize(pen_size)
    turtle.begin_fill()
    # draw circle
    turtle.circle(radius)
    horizontal += 75
    radius += 20
    pen_size += 2
    # moving the turte
    turtle.penup()
    turtle.goto(horizontal, 0)
    turtle.pendown()
    turtle.end_fill()


time.sleep(3)
turtle.clear()
# turtle.write("Ready for more circles?",font=16)
turtle.write("Ready for more circles?", move=False,
             align='center', font=('Arial', 16, 'bold'))
time.sleep(3)
turtle.clear()

for count in range(20):
    c = random.randint(0, 3)
    turtle.fillcolor(colors[c])
    p = random.randint(0, 10)
    turtle.pensize(p)
    turtle.begin_fill()
    # draw circle
    r = random.randint(25, 125)
    turtle.circle(r)
    x = random.randint(-150, 150)
    y = random.randint(-150, 150)

    # moving the turte
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.end_fill()

turtle.done()
