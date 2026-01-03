# More Turtle Graphics, Event Listeners, State and Multiple Instances
from turtle import Turtle, Screen, colormode
import random

is_race_on = False
screen = Screen()
screen.setup(width= 500, height= 400)
user_bet = screen.textinput(title= "Make your bet", prompt= "Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles_list = []
for turtle_index in range(6):
    timy = Turtle(shape= "turtle")
    timy.color(colors[turtle_index])
    timy.penup()
    timy.goto(x= -220, y= -110 + (turtle_index * 50))
    list.append(timy)
    

if user_bet:
    is_race_on = True

while is_race_on:
    random_distance = random.randint(0, 10)
    
    


screen.exitonclick()
