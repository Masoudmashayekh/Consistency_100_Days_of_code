from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISHING_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.left(90)
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        
        
    
    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
        
    def level_up(self):
        if self.ycor() > FINISHING_LINE_Y:
            self.goto(STARTING_POSITION)