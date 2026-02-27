from turtle import Screen, Turtle
from paddle import Paddle


screen = Screen()
screen.bgcolor("black")
screen.setup(width= 800, height= 600)
screen.title("Pong Game")
screen.tracer(0)

r_paddel = Paddle(350, 0)
l_paddel = Paddle(-350, 0)
    
    
screen.listen()
screen.onkey(r_paddel.go_up, "Up")
screen.onkey(r_paddel.go_down, "Down")
screen.onkey(l_paddel.go_up, "w")
screen.onkey(l_paddel.go_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
 

    
    
 






screen.exitonclick()