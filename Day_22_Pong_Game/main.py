from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("black")
screen.setup(width= 800, height= 600)
screen.title("Pong Game")

padel = Turtle()
padel.color("red")
padel.penup()
padel.shape("square")
padel.shapesize(stretch_wid= 5, stretch_len= 1)
padel.goto(350, 0)

 






screen.exitonclick()