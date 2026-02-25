from turtle import Turtle

class ScoreBoard:
    def __init__(self):
        self.score = 0
        
    def board(self):
        Turtle.write(f"Score: {self.score}")
            