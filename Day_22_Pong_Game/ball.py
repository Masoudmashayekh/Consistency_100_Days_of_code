from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        
        
        
    def move(self):
        # self.heading(random(0,45))
        if -290 < self.xcor() < 290 and -290 < self.ycor() < 290:
            new_y = self.ycor() + 1
            new_x = self.xcor() + 1
            self.goto(new_x, new_y)
            