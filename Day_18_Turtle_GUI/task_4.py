# Task 4: Draw a Random Walk
from turtle import Turtle, Screen
import random

# Python tuple (1, 2, 3 ) => A tuple is going to be carved in stone, so you can't change the values like you can with list. (Immutalbe)

colors = ["red", "green", "blue", "orange", "purple", "black", "gray"]
angles = [0, 90, 180, 270]

timmy_the_turtle = Turtle()
timmy_the_turtle.speed(5)


size = 1
for _ in range(20):
    timmy_the_turtle.pensize(size)
    timmy_the_turtle.color(random.choice(colors))
    timmy_the_turtle.forward(30)
    timmy_the_turtle.right(random.choice(angles))
    size += 0.1














screen = Screen()
screen.exitonclick()