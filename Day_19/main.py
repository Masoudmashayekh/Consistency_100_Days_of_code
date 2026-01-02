# More Turtle Graphics, Event Listeners, State and Multiple Instances
from turtle import Turtle, Screen, colormode

screen = Screen()
screen.setup(width= 500, height= 400)
user_bet = screen.textinput(title= "Make your bet", prompt= "Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(5):
    timy = Turtle(shape= "turtle")
    timy.penup()
    timy.goto(x= -220, y= -100 + (i*50))



screen.exitonclick()
