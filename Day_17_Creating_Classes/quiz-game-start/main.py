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
 
    
test = QuizBrain(question_bank)
print(test.question_number)
