import random

print("Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
ANSWER_NUMBER = random.randint(1,100)
print(ANSWER_NUMBER)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").capitalize()
if difficulty == "Easy":
    i = 10
elif difficulty == "Hard":
    i = 5
else:
    print("You type wrong input!!!")
    

    
