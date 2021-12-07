import turtle
import random
x = 0
y = 0
p = random.randint(-200, 200)
q = random.randint(-200, 200)
# Method that controls the button press


def right():
    global x
    global y
    x += movespeed
    if x >= 200:
        x = 200


def left():
    global x
    global y
    x -= movespeed
    if x <= -200:
        x = -200


def up():
    global x
    global y
    y += movespeed
    if y >= 200:
        y = 200


def down():
    global x
    global y
    y -= movespeed
    if y <= -200:
        y = -200


def draw_lunar():
    tur.penup()
    tur.goto(x, y)
    tur.setheading(0)
    tur.pendown()
    for side in range(4):
        tur.forward(50)
        tur.left(90)


def draw_asteroids():
    tur.penup()
    tur.goto(p, q)
    tur.setheading(0)
    tur.pendown()
    for side in range(3):
        tur.forward(30)
        tur.left(120)


# setup screen
screen = turtle .Screen()
screen.setup(500, 500)
screen.tracer(0)  # tell screen to not show automatically
tur = turtle . Turtle()
tur.speed(0)  # draw as fast as possible
tur.width(4)
tur.hideturtle()  # hide the turtle
tur.penup()  # initialize position and variables
tur.goto(0, 0)
tur.pendown()
tur.setheading(0)
movespeed = .03
a_movespeed = .05
# setup listening for key press
turtle.onkeypress(down, "Down")
turtle.onkeypress(up, "Up")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
turtle.listen()

while True:  # game loop
    tur.clear()  # clear screen
    # lunar object
    draw_lunar()
    # asteroid object
    draw_asteroids()
    screen.update()  # update screen
