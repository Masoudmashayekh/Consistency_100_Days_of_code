# Day 18: Turtle Graphics, Tuples and Importing Modules : hirst spot painting
from turtle import Turtle, Screen, colormode
import colorgram # colorgram.py is a Python library that lets you extract colors from images.
import random

colors = colorgram.extract('image.jpg', 5)

colors_list = []
for color in colors:
    rgb = color.rgb
    color.append(rgb)