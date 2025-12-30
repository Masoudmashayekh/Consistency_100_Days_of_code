# Task 4: Draw a Random Walk
from turtle import Turtle, Screen
import random

colors = ["red", "green", "blue", "orange", "purple", "black", "gray"]
angles = [0, 90, 180, 360]
random_trun = random.choice(angles)
random_color = random.choice(colors)



timmy_the_turtle = Turtle()
timmy_the_turtle.speed(5)
timmy_the_turtle.pensize(5)

i = True
while i :
    random_trun = random.choice(angles)
    random_color = random.choice(colors)
    timmy_the_turtle.color(random_color)
    timmy_the_turtle.right(random_trun)
    timmy_the_turtle.forward(20)















screen = Screen()
screen.exitonclick()