from tkinter import *
from quiz_brain import QuizBrain



THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface: 
    
    def  __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg= THEME_COLOR)
        
        self.score_label = Label(text= "Score: 0", fg= "white", bg= THEME_COLOR)
        self.score_label.grid(row=1, column= 2)   
        
        self.canvas = Canvas(width= 300, height= 250, bg= "white")
        self.question_text = self.canvas.create_text(150, 125,width=280, text= "Some question", fill= THEME_COLOR,font= FONT )
        self.canvas.grid(row= 2, column= 1, columnspan= 2, pady= 50) 

        true_image = PhotoImage(file="Day_34_API_Practice/quizzler-app-start/images/true.png")
        self.true_button = Button(image= true_image, highlightthickness=0, command= self.true_pressed)
        self.true_button.grid(row= 3, column= 1)
        
        false_image = PhotoImage(file="Day_34_API_Practice/quizzler-app-start/images/false.png")
        self.false_button = Button(image= false_image, highlightthickness= 0, command= self.false_pressed)
        self.false_button.grid(row= 3, column= 2)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text= q_text)
        
        
    def true_pressed(self):
        self.quiz.check_answer("True")
    
    def false_pressed(self):
        self.quiz.check_answer("False")