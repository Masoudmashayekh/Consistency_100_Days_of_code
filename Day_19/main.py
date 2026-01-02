# More Turtle Graphics, Event Listeners, State and Multiple Instances
from turtle import Turtle, Screen, colormode

screen = Screen()
screen.setup(width= 500, height= 400)
user_bet = screen.textinput(title= "Make your bet", prompt= "Which turtle will win the race? Enter a color: ").lower()

timy = Turtle()



screen.exitonclick()
