from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    new_q = Question(question["text"], question["answer"])
    question_bank.append(new_q)
    
# print(question_bank)
# print(question_bank[0].text)
# print(question_bank[0].answer)  
 
    
quiz = QuizBrain(question_bank)

while quiz.still_has_questions(): # method()
    quiz.next_question() # method()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")