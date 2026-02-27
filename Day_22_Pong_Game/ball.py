from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.turtlesize(stretch_len= 1, stretch_wid= 1)
        self.goto(0, 0)