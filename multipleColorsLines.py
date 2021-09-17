import turtle

# get user input data
initial_len = int(input("Enter the length of the first line: "))
angle = int(input("Enter the turning angle: "))
n = int(input("Enter the number of lines you need: "))
speed = int(input("Enter the animation speed: "))

pen = turtle.Turtle()
pen.speed(speed)
pen.pensize(2)

# start drawing lines
for i in range(n):
    if i % 3 == 0:
        pen.pencolor("red")
        pen.forward(initial_len*i+1)
    elif i % 3 == 1:
        pen.pencolor("green")
        pen.forward(initial_len*i+2)
    elif i % 3 == 2:
        pen.pencolor("blue")
        pen.forward(initial_len*i+3)
    pen.left(angle)
pen.up()
pen.goto(100, -300)
pen.down()
pen.hideturtle()
pen.write("Click on the window to exit...")
turtle.done()
