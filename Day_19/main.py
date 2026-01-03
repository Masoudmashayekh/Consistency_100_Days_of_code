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
    new_turtle = Turtle(shape= "turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x= -220, y= -110 + (turtle_index * 50))
    turtles_list.append(new_turtle)
    

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles_list:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() >= 220:
            is_race_on = False
            winner = turtle
            if winner == user_bet:
                print("You win!")
            else:
                print("You loss!")
            
    
    
    


screen.exitonclick()
