import turtle
from random import randint

wn = turtle.Screen()
wn.bgcolor('green')

colors = ['orange', 'blue', 'white']


def draw_flower():
    i = randint(0, len(colors)-1)
    turtle.color(colors[i])
    turtle.begin_fill()
    for i in range(5):
        turtle.circle(10, 180)
        turtle.right(108)
    turtle.end_fill()


num_flowers = 0

while num_flowers < 30:
    x = randint(-300, 300)
    y = randint(-300, 300)
    draw_flower()
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    num_flowers += 1

wn.exitonclick()
