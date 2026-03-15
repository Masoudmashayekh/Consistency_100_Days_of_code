from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("/Users/masoudmashayekh/Documents/Python/Consistency_100_Days_of_code/Day_24_Files_Directories_Paths/data.txt", mode= "r") as data:
            self.high_score = data.read()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)  
        self.update_scoreboard()
              
        
    def update_scoreboard(self):
         self.clear()
         self.write(f"Score: {self.score} , High Score: {self.high_score}", align= ALIGNMENT, font= FONT)   
        
        
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("/Users/masoudmashayekh/Documents/Python/Consistency_100_Days_of_code/Day_24_Files_Directories_Paths/data.txt", mode= "w") as data:
                data.write(self.high_score)
        self.score = 0
        self.update_scoreboard()
        
        
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align= ALIGNMENT, font= FONT)   
        
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
        
    