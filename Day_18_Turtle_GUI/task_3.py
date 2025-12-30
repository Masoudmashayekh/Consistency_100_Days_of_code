# Task 3
from turtle import Turtle, Screen
import random
colors = ["red", "green", "blue", "orange", "purple", "black", "gray"]
draw_list = [3, 4, 5, 6, 7, 8, 9]


timmy_the_turtle = Turtle()
timmy_the_turtle.speed(1)

for i in range(0, len(draw_list)):
    for _ in range(0, draw_list[i]):
        angle = 360/draw_list[i]
        timmy_the_turtle.color(colors[i])
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)







screen = Screen()
screen.exitonclick()
