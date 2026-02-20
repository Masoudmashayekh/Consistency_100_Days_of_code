from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")



segments = []

for segment in range(3):
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(x= 0 - segment * 20, y= 0)
    segments.append(segment)
    

    


 




screen.exitonclick()