import turtle

def draw_square(inclination):
    i = 1
    pen = turtle.Turtle()
    pen.speed(.5)
    pen.right(inclination)
    while i<=4:
        pen.color("blue")
        pen.forward(100)
        pen.right(90)
        i = i + 1

def draw_flower():
    window = turtle.Screen()
    window.screensize(350,350)
    
    j = 1
    while j <= 360:
        draw_square(j)
        j = j+ 10
    pen1 = turtle.Turtle()
    pen1.color("blue")
    pen1.shape("turtle")
    pen1.goto(0,-300)
    pen1.right(90)
    pen1.stamp()

    window.exitonclick
draw_flower()

    
