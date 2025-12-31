# Task 5: Make a Spirograph
from turtle import Turtle, Screen, colormode
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.speed(0)
colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


for i in range(360):
    timmy_the_turtle.left(i - (i-1))
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.circle(100)









screen = Screen()
screen.exitonclick()