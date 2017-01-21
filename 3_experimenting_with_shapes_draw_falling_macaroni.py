import turtle
from random import random, randint

#Needs improvement

#Reference:https://docs.python.org/3.5/library/turtle.html#turtle.shape

def draw_falling_macaroni():

    #Screen Configuration
    window = turtle.Screen()
    window.bgcolor("yellow")
    window.screensize(500,500)

    #Single Turtle / Pen Used
    macaroni = turtle.Turtle()
    macaroni.color("yellow")
    
    macaroni.pensize(50)
    #Borders
    x = -350
    y = -350
    
    i = 1
    while i<=5:
        
        macaroni.goto(x,y)
        macaroni.right(90)
        macaroni.color("black")
        if i%2 == 0 :
            x = x * -1
        else : 
            y = y * -1
        i = i+1
    
    macaroni.color("yellow")
    macaroni.pensize(1)
  
    #Outer Loop for Pieces of Macaroni
    max_pieces_of_macaroni = 4
    pieces_of_macaroni = 1
    while pieces_of_macaroni <= max_pieces_of_macaroni:

        #Still working on the randomization of the location of the macaroni, so that to much overlap doesn't happen
        #rand_x = randint(-350,350)
        #rand_y = randint(-350,350)
        k = 1
        while k<=4:
            
            rand_x = (300)*(-1)^k
            rand_y = (300)*(-1)^k

            #Go to a random location to draw the piece of macaroni
            macaroni.goto(rand_x,rand_y)
            macaroni.right(randint(-360,360))
    
            macaroni.speed(.2)
            degree_increment = 1
            circle_iterations = 1

            #Inner Loop to create the circle iteration - 1 piece of macaroni
            while (circle_iterations <= 160):
                macaroni.color("black")
                macaroni.circle(75)
                macaroni.right(degree_increment)
                circle_iterations = circle_iterations + degree_increment

            macaroni.color("yellow")
            pieces_of_macaroni = pieces_of_macaroni + 1
            k = k + 1
    window.exitonclick()

#draw_falling_macaroni()


def draw_square(param1):
    brad = turtle.Turtle()
    brad.shape("turtle")
    i = 1
    brad.right(param1)
    while i<=4:
        brad.forward(100)
        brad.right(90)
        i = i+1
    
        
def draw_circle_byrotating_squares():
    #Screen Configuration
    window = turtle.Screen()
    window.bgcolor("yellow")
    window.screensize(500,500)
    j = 0
    while j<360:
        draw_square(j)
        j = j + 10

draw_circle_byrotating_squares()

    

