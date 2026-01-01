# Day 19: More Turtle Graphics, Event Listeners, State and Multiple Instances

from turtle import Turtle, Screen, colormode


timmy = Turtle()
screen = Screen()

def move_forwards():
    timmy.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)




screen.exitonclick()

