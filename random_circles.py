import random
import turtle


class Shape:
    '''
    Shape class to initialise location and color of circle.
    it have only init and str methods to initialise 
    '''

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.color = random.choice(
            ["red", "orange", "yellow", "green", "blue", "purple"])

    def __str__(self):
        loc = "(x="+str(self.x)+", y="+str(self.y)
        col = self.color
        return loc + col


class Circle(Shape):
    '''
    Circle clas inherits shape class.
    It will draw circle.
    x y and rad are the instance variable of the class.
    it have init, str and draw method to draw a circle.
    '''

    def __init__(self, x=0, y=0, rad=0):
        super().__init__(x, y)
        self.rad = rad

    def __str__(self):
        return super().__str__()
        return shape_str + ", rad="+str(self.rad)

    def draw(self, t):
        t.penup()
        t.setpos(self.x, self.y-self.rad)
        t.pendown()
        t.fillcolor(self.color)
        t.begin_fill()
        t.circle(self.rad)
        t.end_fill()


class Display:
    '''
    Diasplay method will display circle on screen.
    it have init and mouse_event methods to catch the mouse events.
    It will call circle class object to get circle data i.e radius, location
    on each click.
    '''

    def __init__(self):
        self.shapes = []
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.hideturtle()
        turtle.delay(0)
        turtle.onscreenclick(self.mouse_event)
        turtle.listen()
        turtle.mainloop()

    def mouse_event(self, x, y):
        new_circ = Circle(x, y, random.randint(10, 50))
        self.shapes.append(new_circ)
        new_circ.draw(self.t)


Display()
