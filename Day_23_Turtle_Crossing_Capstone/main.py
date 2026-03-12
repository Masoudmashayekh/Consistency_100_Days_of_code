import time
from turtle import Screen
from player import Player
from car_manager import CarMaganer
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width= 600, height= 600)
screen.tracer(0)

player = Player()
car_manager = CarMaganer()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()
    
    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()
    
    # Detect seccessful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.lever_up()
        scoreboard.increase_level()
    
    
    
    
    
    
screen.exitonclick()

