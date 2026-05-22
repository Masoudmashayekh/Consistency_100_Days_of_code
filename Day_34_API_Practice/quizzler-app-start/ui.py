from tkinter import *


THEME_COLOR = "#375362"


class QuizInterface:
    
    def  __init__(self):
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg= THEME_COLOR, height= 250, width= 300)
        self.label = Label(text= "score")
        self.label.pack()
        
        
        
        
        
        
        
        self.window.mainloop()
        
