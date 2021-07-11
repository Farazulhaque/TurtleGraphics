import turtle
wn = turtle.Screen()
tess = turtle.Turtle()
tess.pensize(5)
tess.speed(0)
tess.screen.bgcolor('lightgreen')


def lineOfMltySqrs(t, sz, clr1, clr2, clr3, clr4, spc, n):
    for i in range(n):
        t.left(45)
        t.pencolor(clr1)
        t.forward(sz)
        t.left(90)
        t.pencolor(clr2)
        t.forward(sz)
        t.left(90)
        t.pencolor(clr3)
        t.forward(sz)
        t.left(90)
        t.pencolor(clr4)
        t.forward(sz)
        t.up()
        t.left(45)
        t.forward(spc)
        t.down()
    turtle.done()


lineOfMltySqrs(tess, 35, 'red', 'green', 'blue', 'magenta', 30, 6)
