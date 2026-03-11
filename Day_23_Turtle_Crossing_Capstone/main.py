import time
from turtle import Screen
from player import Player
from car_manager import CarMaganer
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width= 600, height= 600)
screen.tracer(0)

palyer = Player()
car_manager = CarMaganer()

screen.listen()
screen.onkey(palyer.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    palyer.level_up()
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()
    
    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(palyer) < 20:
            game_is_on = False
    
    
screen.exitonclick()

