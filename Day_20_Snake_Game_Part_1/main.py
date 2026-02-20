from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")



turtle_list = []

for item in range(3):
    turtle = Turtle(shape="square")
    turtle.color("white")
    turtle.penup()
    turtle.goto(x= 0 - item * 20, y= 0)
    turtle_list.append(item)
    

    


 




screen.exitonclick()