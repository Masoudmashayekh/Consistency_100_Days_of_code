# More Turtle Graphics, Event Listeners, State and Multiple Instances
from turtle import Turtle, Screen, colormode

timy = Turtle()
screen = Screen()
screen.setup(width= 500, height= 400)

text_input = screen.textinput(title= "Make your bet", prompt= "Which turtle will win the race? Enter a color: ")




screen.exitonclick()
