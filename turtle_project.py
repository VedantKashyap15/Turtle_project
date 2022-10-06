import turtle
import random
from turtle import *
t = turtle.Turtle()
turtle.bgcolor("black")
t.color("white")
print("INSTRUCTIONS FOR USING THIS PROGRAM")
print("This program REQUIRES USER INPUT, used for executing simple drawing and cool patterns!")
print("It uses the turtle module which is in built in the python library")
print("****PLEASE SELECT THE BLACK TURTLE SCREEN****, AND THEN FOLLOW AS GIVEN BELOW")
print("Here is the list of command which you can press on the keyboard ")
print("press 'w' 'a' 's' 'd' for moving upwards , leftwards , downwards and rightwards, respectively")
print("press 'r' or 'g' or 'b' to change the pen color to red , green , blue")
print("press 'c' for a random pen color \npress 'f' for random fill color")
print("press:- \n1 for penup\n2 for pendown\n3 for begin fill\n4 for end fill")
print("5 for drawing a square\n6 for drawing a circle")
print("7 for drawing a squarespyrograph\n8 for drawing a circlespyrograph")
print("0 for resetting the screen to default\ne to exit the program")
def randcolor():
    colours=["red","yellow","blue","green","cyan","orange","magenta","purple","brown"]
    x=random.choice(colours)
    t.color(x)

def randfill():
    colours=["red","yellow","blue","green","cyan","orange","magenta","purple","brown"]
    y=random.choice(colours)
    t.fillcolor(y)
    
def up():
    t.setheading(90)
    t.forward(50)

def down():
    t.setheading(270)
    t.forward(50)

def left():
    t.setheading(180)
    t.forward(50)

def right():
    t.setheading(0)
    t.forward(50)

def beginfill():
    t.begin_fill()

def endfill():
    t.end_fill()

def penup():
    t.penup()

def pendown():
    t.pendown()
    
def square():
    for i in range(0,4):
        t.forward(50)
        t.left(90)
def circle():
    t.circle(50)

def squarespyrograph():
    t.reset()
    turtle.bgcolor("black")
    t.speed(0)
    for i in range(0,3):
        for colors in ["red","yellow","blue","green","cyan","white","orange","purple","magenta","brown"]:
            t.color(colors)
            t.left(12)
            t.forward(150)
            t.left(90)
            t.forward(150)
            t.left(90)
            t.forward(150)
            t.left(90)
            t.forward(150)
            t.left(90)

def circlespyrograph():
    t.reset()
    turtle.bgcolor("black")
    t.speed(0)
    for i in range(0,3):
        for colors in ["red","yellow","blue","green","cyan","white","orange","purple","magenta","brown"]:
            t.color(colors)
            t.left(12)
            t.circle(100)

def colorR():
    t.color("red")
def colorB():
    t.color("blue")
def colorG():
    t.color("green")

def reset():
    t.reset()
    t.color("white")
def endscreen():
    turtle.bye()
    
turtle.onkey(up, "w")
turtle.onkey(down, "s")
turtle.onkey(left, "a")
turtle.onkey(right, "d")
turtle.onkey(square, "5")
turtle.onkey(circle, "6")
turtle.onkey(colorR, "r")
turtle.onkey(colorG, "g")
turtle.onkey(colorB, "b")
turtle.onkey(randcolor, "c")
turtle.onkey(randfill, "f")
turtle.onkey(beginfill, "3")
turtle.onkey(endfill, "4")
turtle.onkey(penup, "1")
turtle.onkey(pendown, "2")
turtle.onkey(squarespyrograph, "7")
turtle.onkey(circlespyrograph, "8")
turtle.onkey(reset, "0")
turtle.onkey(endscreen, "e")
turtle.listen()
