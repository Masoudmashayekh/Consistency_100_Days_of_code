# Task 2
import turtle # Keyword & Module name
# timmy_the_turtle = turtle.Turtle()

# from turtle import Turtle, Screen #  Keyword & Module name & Keyword & Thing in Module
# from turtle import *   => You can use everything that's in that module (But it is not usefull)
# import turtle as t => keyword, module name, keyword, alias name
timmy_the_tutle = turtle.Turtle()
timmy_the_tutle.pen(speed = 1)

i = 50
while i > 0:
    timmy_the_tutle.pendown()
    timmy_the_tutle.forward(5)
    timmy_the_tutle.penup()    
    timmy_the_tutle.forward(5)
    i -= 1
    
    
screen = turtle.Screen()
screen.exitonclick()