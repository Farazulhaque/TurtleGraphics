# import package
import turtle
pen = turtle.Turtle()

# this function draws star shape


def drawing(a_turtle, side_len):
    # loop 5 times since star has 5 lines
    for i in range(5):
        # create length of side_len for each line
        a_turtle.forward(side_len)
        # after each line turn 144 degree right
        a_turtle.right(144)
    # return nothing
    return None


# calling drawing function
drawing(pen, 200)
turtle.done()
