# Day 19: More Turtle Graphics, Event Listeners, State and Multiple Instances, Higher Order Functions

from turtle import Turtle, Screen, colormode


timmy = Turtle()
screen = Screen()

def move_forwards():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)
    
def clear():
    timmy.reset()

def counter_clockwise():
    timmy.left(5)

def clockwise():
    timmy.right(5)

screen.listen()
screen.onkey(key="w", fun= move_forwards)
screen.onkey(key="s", fun= move_backward)
screen.onkey(key="a", fun= counter_clockwise)
screen.onkey(key="d", fun= clockwise)
screen.onkey(key="c", fun= clear)




screen.exitonclick()

