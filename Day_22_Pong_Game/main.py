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

def padel_up():
    y_position = padel.ycor() + 20
    padel.goto(350, y_position)
    
def padel_down():
    y_position = padel.ycor() - 20
    padel.goto(350, y_position)
    
    
screen.listen()
screen.onkey(padel_up, "Up")
screen.onkey(padel_down, "Down")



game_is_on = True
while game_is_on:
    screen.update()  
    screen.exitonclick()
    
    
 






screen.exitonclick()