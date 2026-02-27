from turtle import Screen
from paddle import Paddle
from ball import Ball
import time 

screen = Screen()
screen.bgcolor("black")
screen.setup(width= 800, height= 600)
screen.title("Pong Game")
screen.tracer(0)

r_paddel = Paddle((350, 0))
l_paddel = Paddle((-350, 0))

ball = Ball()    
    
screen.listen()
screen.onkey(r_paddel.go_up, "Up")
screen.onkey(r_paddel.go_down, "Down")
screen.onkey(l_paddel.go_up, "w")
screen.onkey(l_paddel.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ball.move()
    screen.update()
    
    # Detect collision wiht wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
 
    # Detect collision with paddel
    if ball.distance(r_paddel) < 50 and ball.xcor() > 320 or ball.distance(l_paddel) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    if ball.distance(r_paddel) > 50 and ball.xcor() > 370 or ball.distance(l_paddel) > 50 and ball.xcor() < -370:
        ball.game_rest()
 






screen.exitonclick()