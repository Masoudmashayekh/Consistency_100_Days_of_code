# Task 4: Draw a Random Walk
import turtle as t
import random

# Python tuple (1, 2, 3 ) => A tuple is going to be carved in stone, so you can't change the values like you can with list. (Immutalbe)

angles = [0, 90, 180, 270]

timmy_the_turtle = t.Turtle()
t.colormode(255)
timmy_the_turtle.speed(5)

def random_color():
    color = []
    for _ in range(3):
        color_random = random.randrange(0, 255)
        color.append(color_random)
    return (color[0], color[1], color[2])

size = 1
for _ in range(200):
    timmy_the_turtle.pensize(size)
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.forward(30)
    timmy_the_turtle.right(random.choice(angles))
    size += 0.1














screen = t.Screen()
screen.exitonclick()