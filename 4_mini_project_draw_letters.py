import turtle
start = -350

def draw_semi_circle(x,y):
    drawing_pen1 = turtle.Turtle()
    drawing_pen1.color("white")
    drawing_pen1.goto(x,y)
    drawing_pen1.color("black")
    i = 1
    while i <= 180:
        drawing_pen1.right(1)
        drawing_pen1.forward(.25)
        i = i + 1
    return (start)

def print_a(start):
    drawing_pen = turtle.Turtle()
    drawing_pen.speed(1)
    drawing_pen.color("white")
    drawing_pen.goto(start,0)
    drawing_pen.left(60)
    drawing_pen.color("black")
    drawing_pen.forward(75)
    drawing_pen.right(120)
    drawing_pen.forward(75)
    drawing_pen.right(120)
    drawing_pen.color("white")
    drawing_pen.forward(75)
    drawing_pen.color("black")
    drawing_pen.right(120)
    drawing_pen.forward(37)
    drawing_pen.right(60)
    drawing_pen.forward(37)
    return (75 + 15)

def print_b(start):
    drawing_pen = turtle.Turtle()
    drawing_pen.speed(1)
    drawing_pen.color("white")
    drawing_pen.goto(start,0)
    drawing_pen.left(90)
    drawing_pen.color("black")
    drawing_pen.forward(round(1.732*37.5,0))
    drawing_pen.right(90)

    draw_semi_circle(start,round(1.732*37.5,0))
    draw_semi_circle(start,round(1.732*37.5/2,0))

    return 0

def print_letters():
    #Window and Pen Configuration
    window = turtle.Screen()
    window.screensize(350,350)
    window.bgcolor("white")
    start = -350
    

    start = start + print_a(start)
    start = start + print_b(start)
    #Get User Input

    #Breakdown Letters and Call Respective Functions

    #Spacing Algorithm
print_letters()
