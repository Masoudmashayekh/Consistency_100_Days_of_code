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
    
    
print(rgb_colors_list)