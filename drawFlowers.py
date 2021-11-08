import turtle

# defines turtle stuff DONE
t = turtle.Turtle()
t.pensize(3)
t.color('green')
t.shape('turtle')
wn = turtle.Screen()

global x
global y
x = 100
y = 100


def click(a, b):
    x = a
    y = b
    t.penup()
    t.goto(x, y)
    t.pendown()
# function for stem DONE


def stem():
    for i in range(1):
        t.pencolor("green")
        t.pendown()
        t.right(90)
        t.forward(200)
        t.left(90)


def sun():
    for i in range(50):
        t.pendown()
        t.speed(0)
        t.color("yellow")
        t.begin_fill()
        t.forward(200)
        t.left(70)
        t.end_fill()
        t.setheading(0)


def flower1():
    t.speed(0)

    for i in range(50):
        t.right(100)
        t.begin_fill()
        t.color("red")
        t.forward(300)
        t.left(170)
        t.end_fill()
        t.setheading(0)


def flower2():
    t.speed(0)
    for i in range(20):
        t.right(100)
        t.fillcolor('yellow')
        t.begin_fill()
        t.circle(300, 70)
        t.left(110)
        t.circle(300, 70)
        t.end_fill()
        # t.setheading(0)


def flower3():
    t.speed(0)

    for i in range(20):
        t.right(100)
        t.fillcolor('blue')
        t.begin_fill()
        t.circle(300, 70)
        t.left(110)
        t.circle(300, 70)
        t.end_fill()
        # t.setheading(0)


wn.onkey(stem, "t")
wn.onkey(sun, "s")
wn.onkey(flower1, "1")
wn.onkey(flower2, "2")
wn.onkey(flower3, "3")
wn.listen()
# turtle.onscreenclick(flower1)
# turtle.onscreenclick(flower2)
# turtle.onscreenclick(flower3)
turtle.onscreenclick(click)


wn.mainloop()
