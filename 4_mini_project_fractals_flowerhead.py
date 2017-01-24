import turtle

def draw_serpinski_fractal(pen,size,iterations):

    if iterations > 0:
        pen.left(120)
        for i in range(0,3):
            pen.forward(size/2)
            draw_serpinski_fractal(pen,size/2,iterations-1)
            pen.forward(size/2)
            if i < 2 :
                pen.right(120)
            else:
                pen.left(120)
            
    

window = turtle.Screen()
window.bgcolor("white")

draw_pen = turtle.Turtle()
draw_pen.color("black")
draw_pen.speed(100)

i = 1
while i <= 360:
    draw_serpinski_fractal(draw_pen,200,4)
    draw_pen.forward(200)
    draw_pen.left(120)
    draw_pen.forward(400)
    draw_pen.left(120)
    draw_pen.forward(400)
    draw_pen.left(120)
    draw_pen.forward(200)
    draw_pen.right(36)
    i = i + 36


