# Day 18: Turtle Graphics, Tuples and Importing Modules : hirst spot painting
from turtle import Turtle, Screen, colormode
import colorgram # colorgram.py is a Python library that lets you extract colors from images.
import random
from pathlib import Path

BASE_DIR = Path(__file__).parent
image_path = BASE_DIR / "./images/image.jpg"

colors = colorgram.extract(image_path, 15)


rgb_colors_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)
    rgb_colors_list.append(rgb)
    

timmy_the_turtle = Turtle()
timmy_the_turtle.hideturtle()
timmy_the_turtle.speed("fastest")
colormode(255)


for y in range(-200, 201, 40):
    for x in range(-200, 201, 40):
        timmy_the_turtle.penup()
        timmy_the_turtle.goto(x, y)
        timmy_the_turtle.pendown()
        timmy_the_turtle.dot(20, random.choice(rgb_colors_list))



screen = Screen()
screen.exitonclick()