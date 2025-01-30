import turtle
from turtle import *

circle = turtle.Turtle()
circle.color("yellow")
circle.shape("turtle")
circle.pensize(5)
circle.speed(1000)

t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.speed(500)

t1 = turtle.Turtle()
t1.shape("turtle")
t1.color("blue")
t1.speed(500)

t2 = turtle.Turtle()
t2.shape("turtle")
t2.color("red")
t2.speed(500)

t3 = turtle.Turtle()
t3.shape("turtle")
t3.color("pink")
t3.speed(500)

t4 = turtle.Turtle()
t4.shape("turtle")
t4.color("orange")
t4.speed(500)

t5 = turtle.Turtle()
t5.shape("turtle")
t5.color("gray")
t5.speed(500)

def circles(numcircles):
    circle.begin_fill()
    circle.fillcolor("gray")
    for i in range(numcircles):
        circle.circle(20)
        circle.penup()
        circle.forward(50)
        circle.pendown()
    circle.end_fill()

circle.penup()
circle.goto(0,-50)
circles((5))
circle.penup()
circle.goto(50, 130)
circle.pendown()
circles(3)
circle.penup()
circle.goto(100, 280)
circle.pendown()
circles(1)

def turtle_zero():
    t.penup()          # set up the turtle
    t.goto(0, -40) # start position
    t.pendown()
    i = 0
    while i <150:
        i += 50
        t.goto(i,150) #top circle 1
        t.goto(0,-40)

def turtle_one():
    t1.penup()          # set up the turtle
    t1.goto(50, -40) # start position
    t1.pendown()
    i = 0
    while i <150:
        i += 50
        t1.goto(i,150) #top circle 1
        t1.goto(50,-40)

def turtle_two():
    t2.penup()  # set up the turtle
    t2.goto(100, -40)  # start position
    t2.pendown()
    i = 0
    while i < 150:
        i += 50
        t2.goto(i, 150)  # top circle 1
        t2.goto(100, -40)

def turtle_three():
    t3.penup()  # set up the turtle
    t3.goto(150, -40)  # start position
    t3.pendown()
    i = 0
    while i < 150:
        i += 50
        t3.goto(i, 150)  # top circle 1
        t3.goto(150, -40)

def turtle_four():
    t4.penup()  # set up the turtle
    t4.goto(200, -40)  # start position
    t4.pendown()
    i = 0
    while i < 150:
        i += 50
        t4.goto(i, 150)  # top circle 1
        t4.goto(200, -40)

def turtle_five():
    t5.penup()  # set up the turtle
    t5.goto(50, 150)  # start position
    t5.pendown()
    i = 0
    while i < 100:
        i += 50
        t5.goto(100, 300)  # top circle 1
        t5.goto(i+50, 150)

turtle_zero()
turtle_one()
turtle_two()
turtle_three()
turtle_four()
#layer 2
turtle_five()
turtle.penup()
turtle.goto(-300, 300)
turtle.pendown()
turtle.write("Simple Neural Network", move=True, align="left", font=("Arial", 32, "bold"))
turtle.done()