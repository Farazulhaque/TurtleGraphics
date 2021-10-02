from turtle import *
import turtle

Kat = turtle.Turtle()
Kat.speed(0)


def spinPolygon(tortoise, nSides, sidelength, angle, nCopies):
    for i in range(nCopies):
        for j in range(nSides):
            tortoise.forward(sidelength)
            tortoise.left(90)
        tortoise.left(angle)


# spinPolygon(Kat, 4, 50, 30, 5)

# spinPolygon(Kat, 4, 50, -30, 3)

spinPolygon(Kat, 4, 50, 10, 100)

turtle.done()
