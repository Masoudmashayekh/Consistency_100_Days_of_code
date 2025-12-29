# asking the questions.
# checking if the answer was correct.
# checking if we're the end of the quiz.
class QuizBrain():
    
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
 
    def next_question(self):
        self.question = self.question_list[self.question_number].text
        self.answer = self.question_list[self.question_number].answer
        self.question_number += 1
        self.user_answer = input(f"Q.{self.question_number}: {self.question} (True/False)?:")
        