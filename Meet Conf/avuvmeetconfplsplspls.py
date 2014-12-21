import turtle
turtle.hideturtle()
turtle.speed(0)
turtle.colormode(255)
from random import randrange
def square(x,y):
    turtle.begin_fill()
    turtle.fillcolor(randrange(0,255),randrange(0,255),randrange(0,255))
    for n in range(1,4):
        turtle.penup()
        turtle.goto(x,y)
        turtle.goto(x+50,y)
        turtle.goto(x+50,y+50)
        turtle.goto(x,y+50)
        turtle.goto(x,y)
        turtle.penup()
    turtle.end_fill()
def circle(x,y): 
    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()
    turtle.begin_fill()
    turtle.fillcolor(randrange(0,255),randrange(0,255),randrange(0,255))
    turtle.circle(25)
    turtle.end_fill()
    
def crazy_stuff(x,y):
    for n in range(1,100):
        turtle.pensize(randrange(0,100))
        turtle.pencolor((randrange(0,255),randrange(0,255),randrange(0,255)))
        turtle.goto(randrange(-500,500),randrange(-500,500))
    turtle.clear()
    turtle.onscreenclick(crazy_stuff)
    turtle.onscreenclick(break,3)
turtle.onscreenclick(square)
turtle.onscreenclick(circle,3)
turtle.onscreenclick(crazy_stuff,2)
turtle.mainloop()
